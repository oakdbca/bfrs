# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0020_auto_20170718_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfire',
            name='assistance_details',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='assistance_req',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='communications',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='reviewed_by',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='reviewed_date',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='time_to_control',
        ),
        migrations.RemoveField(
            model_name='bushfiresnapshot',
            name='assistance_details',
        ),
        migrations.RemoveField(
            model_name='bushfiresnapshot',
            name='assistance_req',
        ),
        migrations.RemoveField(
            model_name='bushfiresnapshot',
            name='communications',
        ),
        migrations.RemoveField(
            model_name='bushfiresnapshot',
            name='reviewed_by',
        ),
        migrations.RemoveField(
            model_name='bushfiresnapshot',
            name='reviewed_date',
        ),
        migrations.RemoveField(
            model_name='bushfiresnapshot',
            name='time_to_control',
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='cause',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bfrs.Cause', verbose_name=b'Fire Cause'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='cause_state',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, b'Known'), (2, b'Possible')], null=True, verbose_name=b'Fire Cause State (Known/Possible)'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='damage_unknown',
            field=models.BooleanField(default=False, verbose_name=b'Damages to report?'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='dispatch_aerial',
            field=models.NullBooleanField(verbose_name=b'Aerial suppression dispatched'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='dispatch_aerial_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Aerial suppression dispatch date'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='dispatch_pw',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, b'Yes'), (2, b'No')], null=True, verbose_name=b'P&W Resource dispatched'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='dispatch_pw_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'P&W Resource dispatch date'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='fire_behaviour_unknown',
            field=models.BooleanField(default=False, verbose_name=b'Fuel and fire behaviour'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='fire_contained_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date fire Contained'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='fire_controlled_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date fire Controlled'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='fire_detected_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date and time fire detected'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='fire_safe_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date fire inactive'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='first_attack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bushfire_first_attack', to='bfrs.Agency', verbose_name=b'Initial Attack Agency'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='injury_unknown',
            field=models.BooleanField(default=False, verbose_name=b'Injuries to report?'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='other_cause',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'Other Fire Cause'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='other_first_attack',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Other Initial Attack Agency'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='other_tenure',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, b'Private'), (2, b'Crown')], null=True, verbose_name=b'Other Tenure (Crown/Private)'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='tenure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bfrs.Tenure', verbose_name=b'Tenure of Ignition Point'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='cause',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bfrs.Cause', verbose_name=b'Fire Cause'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='cause_state',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, b'Known'), (2, b'Possible')], null=True, verbose_name=b'Fire Cause State (Known/Possible)'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='damage_unknown',
            field=models.BooleanField(default=False, verbose_name=b'Damages to report?'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='dispatch_aerial',
            field=models.NullBooleanField(verbose_name=b'Aerial suppression dispatched'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='dispatch_aerial_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Aerial suppression dispatch date'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='dispatch_pw',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, b'Yes'), (2, b'No')], null=True, verbose_name=b'P&W Resource dispatched'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='dispatch_pw_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'P&W Resource dispatch date'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='fire_behaviour_unknown',
            field=models.BooleanField(default=False, verbose_name=b'Fuel and fire behaviour'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='fire_contained_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date fire Contained'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='fire_controlled_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date fire Controlled'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='fire_detected_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date and time fire detected'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='fire_safe_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Date fire inactive'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='first_attack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bushfiresnapshot_first_attack', to='bfrs.Agency', verbose_name=b'Initial Attack Agency'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='injury_unknown',
            field=models.BooleanField(default=False, verbose_name=b'Injuries to report?'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='other_cause',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'Other Fire Cause'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='other_first_attack',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Other Initial Attack Agency'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='other_tenure',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, b'Private'), (2, b'Crown')], null=True, verbose_name=b'Other Tenure (Crown/Private)'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='tenure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bfrs.Tenure', verbose_name=b'Tenure of Ignition Point'),
        ),
    ]