# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-07 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20171206_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
