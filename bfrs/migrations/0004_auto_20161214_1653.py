# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-14 08:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0003_auto_20161214_1620'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='activity2',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='activity2',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='activity2',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='cause',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='first_attack',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='fuel_type',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='tenure',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='frb_effect',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='waterbomb_effect',
        ),
        migrations.RemoveField(
            model_name='firstattackagency',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='firstattackagency',
            name='final_control',
        ),
        migrations.RemoveField(
            model_name='firstattackagency',
            name='first_attack',
        ),
        migrations.RemoveField(
            model_name='firstattackagency',
            name='hazard_mgt',
        ),
        migrations.RemoveField(
            model_name='firstattackagency',
            name='initial_control',
        ),
        migrations.RemoveField(
            model_name='initial',
            name='authorised_by',
        ),
        migrations.RemoveField(
            model_name='initial',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='initial',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='initial',
            name='field_officer',
        ),
        migrations.RemoveField(
            model_name='initial',
            name='modifier',
        ),
        migrations.RemoveField(
            model_name='origin',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='reporter',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='reporter',
            name='cause',
        ),
        migrations.RemoveField(
            model_name='reporter',
            name='prescription',
        ),
        migrations.RemoveField(
            model_name='reporter',
            name='source',
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='activitytype',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='aerialforces',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='agency',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='areaburnt',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='attendingorganisation',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='cause',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='direction',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='firebehaviour',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='frbeffect',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='fueltype',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='groundforces',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='investigationtype',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='legal',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='legalresulttype',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='organisation',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='priorityrating',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='privatedamage',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='privatedamagetype',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'default_permissions': ('add', 'change', 'view')},
        ),
        migrations.AlterModelOptions(
            name='publicdamage',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='publicdamagetype',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='responsetype',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tenure',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='waterbombeffect',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ['name']},
        ),
        migrations.DeleteModel(
            name='Activity2',
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.DeleteModel(
            name='Effect',
        ),
        migrations.DeleteModel(
            name='FirstAttackAgency',
        ),
        migrations.DeleteModel(
            name='Initial',
        ),
        migrations.DeleteModel(
            name='Origin',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
