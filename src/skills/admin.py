from django.contrib import admin
from .models import *


@admin.register(Skills)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'skills_title', 'skills_text', 'skills_slug')