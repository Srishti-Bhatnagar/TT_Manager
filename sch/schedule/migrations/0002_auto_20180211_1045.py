# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-11 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='Sid',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Tid',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
