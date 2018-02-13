# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-13 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_auto_20180213_0958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'ordering': ('year',)},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('subject_code',)},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('Tid',)},
        ),
        migrations.AlterField(
            model_name='schedule',
            name='Sid',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together=set([('sem', 'stream')]),
        ),
    ]
