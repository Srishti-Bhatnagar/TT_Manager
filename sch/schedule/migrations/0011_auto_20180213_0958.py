# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-13 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20180213_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(default=b'', max_length=5, primary_key=True, serialize=False),
        ),
    ]
