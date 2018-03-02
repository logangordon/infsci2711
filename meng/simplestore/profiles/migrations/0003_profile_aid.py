# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-06 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20171204_2215'),
        ('profiles', '0002_auto_20171206_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='checkout.Address'),
            preserve_default=False,
        ),
    ]