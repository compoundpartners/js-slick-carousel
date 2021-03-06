# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-25 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_slick', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slickcarouselwrappedslide',
            name='caption',
            field=models.CharField(blank=True, max_length=256, verbose_name='Content caption'),
        ),
        migrations.AlterField(
            model_name='slickcarouselwrappedslide',
            name='title',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='Plugin title'),
            preserve_default=False,
        ),
    ]
