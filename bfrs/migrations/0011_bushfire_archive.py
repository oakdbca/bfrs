# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0010_bushfire_park_trail_impacted'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='archive',
            field=models.BooleanField(default=False, verbose_name=b'Archive report'),
        ),
    ]