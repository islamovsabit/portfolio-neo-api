# Generated by Django 4.2.4 on 2023-10-13 05:47

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_icon', models.CharField(max_length=150, verbose_name='значок контакта')),
                ('contact_name', models.CharField(max_length=150, verbose_name='имя контакта')),
                ('contact_text', models.CharField(max_length=200, verbose_name='текстовый контакт')),
                ('contact_slug', autoslug.fields.AutoSlugField(editable=True, populate_from='contact_name', unique=True, verbose_name='слизняк контакт')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакт',
            },
        ),
    ]