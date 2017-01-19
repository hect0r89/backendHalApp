# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contacts.Phone', verbose_name='Phone'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
