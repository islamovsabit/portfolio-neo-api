from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


from django.contrib import admin
from .models import PortfolioCategory, Portfolio


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'portfolio_slug', 'slug')
    prepopulated_fields = {'slug': ('portfolio_slug',)}


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
                      'id',
                      'uploader_name',
                      'portfolio_title',
                      'portfolio_data',
                      'portfolio_slug'
                    )
