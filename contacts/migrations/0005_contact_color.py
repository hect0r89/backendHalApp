# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20170119_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='color',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
