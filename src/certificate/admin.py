# from django.contrib import admin
from django.contrib import admin
from django.utils.html import format_html
from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificate_name', 'certificate_created', 'certificate_img')
    list_display_links = ('id', 'certificate_name')  # Make 'certificate_name' a link to the detail view

    def certificate_img(self, obj):
        return format_html('<a href="{}"><img src="{}" width="110" height="78" /></a>', obj.certificate_image.url, obj.certificate_image.url)

    certificate_img.short_description = 'Certificate Image'


admin.site.register(Certificate, CertificateAdmin)
