# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-31 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0031_bushfire_area_unknown'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='alias',
            field=models.CharField(default=1, max_length=200, unique=True, verbose_name=b'Equiv. name in SSS'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='district',
            name='archive_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]