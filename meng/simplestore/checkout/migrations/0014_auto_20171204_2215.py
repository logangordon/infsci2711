# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-04 22:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_auto_20170831_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_method',
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]
