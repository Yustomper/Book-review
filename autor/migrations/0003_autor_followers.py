# Generated by Django 5.0.7 on 2024-07-27 21:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_autor_photo_follow'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='followers',
            field=models.ManyToManyField(related_name='following', through='autor.Follow', to=settings.AUTH_USER_MODEL),
        ),
    ]