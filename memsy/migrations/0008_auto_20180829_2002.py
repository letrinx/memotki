# Generated by Django 2.1 on 2018-08-29 20:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memsy', '0007_auto_20180828_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mems',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
