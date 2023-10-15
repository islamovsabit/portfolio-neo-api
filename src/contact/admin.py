from django.contrib import admin
from .models import *


@admin.register(Contact)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
                    'id',
                    'contact_icon',
                    'contact_name',
                    'contact_text',
                    'contact_slug'
                    )
