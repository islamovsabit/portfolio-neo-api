from django.db import models
from autoslug import AutoSlugField
# Create your models here.


class Contact(models.Model):
    contact_icon = models.CharField(max_length=150, verbose_name="значок контакта")
    contact_name = models.CharField(max_length=150, verbose_name="имя контакта")
    contact_text = models.CharField(max_length=200, verbose_name="текстовый контакт")
    contact_slug = AutoSlugField(unique=True, populate_from='contact_name', verbose_name="слизняк контакт", editable=True)

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакт"
