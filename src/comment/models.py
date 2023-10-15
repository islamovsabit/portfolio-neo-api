from django.db import models


class Email(models.Model):
    user_name = models.CharField(max_length=150, verbose_name="имя пользователя")
    user_email = models.EmailField(max_length=200, verbose_name="адрес электронной почты")
    user_message = models.TextField(max_length=900, verbose_name="сообщение пользователя")

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "почтовая форма"
        verbose_name_plural = "почтовая форма"
