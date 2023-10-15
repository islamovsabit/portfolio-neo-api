from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


class PortfolioCategoryView(ListAPIView):
    try:
        queryset = PortfolioCategory.objects.all()
        serializer_class = PortfolioCategorySerializer
    except PortfolioCategory.DoesNotExist:
        raise Http404


class PortfolioView(ListAPIView):
    try:
        queryset = Portfolio.objects.all()
        serializer_class = PortfolioSerializer
    except Portfolio.DoesNotExist:
        raise Http404


class PortfolioFilterById(ListAPIView):
    def get(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
            serializer = PortfolioSerializer(portfolio)
            return Response(serializer.data)
        except Portfolio.DoesNotExist:
            return Response(
                {"detail": "Portfolio item not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class PortfolioSlugView(APIView):
    def get_object(self, portfolio_slug):
        try:
            return Portfolio.objects.get(portfolio_slug=portfolio_slug)
        except Portfolio.DoesNotExist:
            raise Http404

    def get(self, request, portfolio_slug):
        portfolio = self.get_object(portfolio_slug)
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)


class CategoryIdPortfolioAPIView(APIView):
    def get(self, request, portfolio_category, pk):
        try:
            portfolio = Portfolio.objects.get(portfolio_category=portfolio_category, pk=pk)
        except Portfolio.DoesNotExist:
            return Response({"detail": "Portfolio not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)


class PortfoliosByCategoryAPIView(APIView):
    def get(self, request, portfolio_slug):
        try:
            portfolio_category = PortfolioCategory.objects.get(portfolio_slug=portfolio_slug)
            portfolios = Portfolio.objects.filter(portfolio_category=portfolio_category)
            serialized_data = [
                {
                    'id': portfolio.id,
                    'uploader_name': portfolio.uploader_name,
                    'portfolio_title': portfolio.portfolio_title,
                    'portfolio_text': portfolio.portfolio_text,
                    'portfolio_link': portfolio.portfolio_link,
                    'portfolio_img': f"http://127.0.0.1:8000{portfolio.portfolio_image.url}",
                    'portfolio_video_url': f"http://127.0.0.1:8000{portfolio.portfolio_video.url}",
                    'portfolio_data': portfolio.portfolio_data,
                    'portfolio_slug': portfolio.portfolio_slug,
                    'portfolio_category': f"{portfolio.portfolio_category.id}",
                    'portfolio_category_slug': {
                        'id': f"{portfolio.portfolio_category.id}",
                        'slug': f"{portfolio_category}"
                    }
                }
                for portfolio in portfolios
            ]

            return Response(serialized_data)
        except PortfolioCategory.DoesNotExist:
            return Response({'detail': 'Portfolio category not found'}, status=status.HTTP_404_NOT_FOUND)
