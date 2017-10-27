# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_sessions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessions',
            options={'verbose_name_plural': 'Sessions'},
        ),
        migrations.AddField(
            model_name='sessions',
            name='booked_time',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Availability'),
        ),
    ]
