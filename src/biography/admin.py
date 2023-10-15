from django.contrib import admin
from .models import *


@admin.register(Biography)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'biography_title', 'biography_text', 'biography_slug')