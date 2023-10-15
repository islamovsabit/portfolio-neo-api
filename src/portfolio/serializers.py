from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *


class PortfolioCategorySerializer(ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ('id', "portfolio_slug", 'slug')


class PortfolioSlug(ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ('id', 'slug')


class PortfolioSerializer(ModelSerializer):
    portfolio_category_slug = PortfolioSlug(source='portfolio_category')

    def get_portfolio_slug(self, obj):
        return obj.portfolio_category_slug.slug

    class Meta:
        model = Portfolio
        fields = ('id',
                  'uploader_name',
                  'portfolio_title',
                  'portfolio_text',
                  'portfolio_link',
                  'portfolio_img',
                  'portfolio_video_url',
                  'portfolio_data',
                  'portfolio_slug',
                  'portfolio_category',
                  'portfolio_category_slug')
    portfolio_img = SerializerMethodField()

    def get_portfolio_img(self, obj):
        return f"http://127.0.0.1:8000{obj.portfolio_image.url}"
    portfolio_video_url = SerializerMethodField()

    def get_portfolio_video_url(self, obj):
        return f"http://127.0.0.1:8000{obj.portfolio_video.url}"
