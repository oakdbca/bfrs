# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-14 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bushfire',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
    ]