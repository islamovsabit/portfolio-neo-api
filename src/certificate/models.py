from django.db import models
from autoslug import AutoSlugField


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=100, verbose_name="имя сертификата")
    certificate_created = models.CharField(max_length=50, verbose_name="сертификат создан")
    certificate_image = models.ImageField(upload_to="media/photo/portfolio", verbose_name="изображение портфолио", blank=True, null=True)
    certificate_slug = AutoSlugField(unique=True, populate_from='certificate_name', verbose_name="слизняк сертификат", editable=True)

    def __str__(self):
        return self.certificate_name

    class Meta:
        verbose_name = "сертификат"
        verbose_name_plural = "сертификат"

