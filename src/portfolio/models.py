from django.db import models
from autoslug import AutoSlugField


class PortfolioCategory(models.Model):
    portfolio_slug = models.CharField(max_length=50)
    slug = AutoSlugField(unique=True, populate_from='portfolio_slug', editable=True)

    def __str__(self):
        return self.portfolio_slug

    class Meta:
        verbose_name = "слизняк портфолио"
        verbose_name_plural = "слизняк портфолио"


class Portfolio(models.Model):
    uploader_name = models.CharField(max_length=50, verbose_name="имя загрузившего")
    portfolio_title = models.CharField(max_length=100, verbose_name="название портфолио")
    portfolio_text = models.TextField(max_length=300, verbose_name="текст портфолио", blank=True, null=True)
    portfolio_link = models.CharField(max_length=300, verbose_name="ссылка на портфолио")
    portfolio_image = models.ImageField(upload_to="media/photo/portfolio", verbose_name="изображение портфолио", blank=True, null=True)
    portfolio_video = models.FileField(upload_to='media/video/portfolio', verbose_name="портфолио видео", blank=True, null=True)
    portfolio_data = models.DateTimeField(auto_now_add=True)
    portfolio_slug = AutoSlugField(unique=True, populate_from='portfolio_title', verbose_name="слизняк портфолио", editable=True)
    portfolio_category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, verbose_name="категория портфолио")

    def __str__(self):
        return self.portfolio_title

    class Meta:
        verbose_name = "портфолио"
        verbose_name_plural = "портфолио"
