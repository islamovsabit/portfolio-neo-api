from django.db import models
from autoslug import AutoSlugField


class Skills(models.Model):
    skills_title = models.CharField(max_length=70, verbose_name="название навыка")
    skills_text = models.CharField(max_length=150, verbose_name="текст навыков")
    skills_slug = AutoSlugField(unique=True, populate_from='skills_title', verbose_name="слизняк навыка", editable=True)

    def __str__(self):
        return self.skills_title

    class Meta:
        verbose_name = "навыки"
        verbose_name_plural = "навыки"
