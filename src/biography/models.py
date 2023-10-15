from django.db import models
from autoslug import AutoSlugField


class Biography(models.Model):
    biography_title = models.CharField(max_length=80, verbose_name="название биографии")
    biography_text = models.CharField(max_length=80, verbose_name="текст биографии")
    biography_slug = AutoSlugField(unique=True, populate_from='biography_title', verbose_name="слизняк биография", editable=True)

    def __str__(self):
        return self.biography_title

    class Meta:
        verbose_name = "Биографии"
        verbose_name_plural = "Биографии"
