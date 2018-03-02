# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-05 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='perex',
        ),
        migrations.AddField(
            model_name='product',
            name='inventoryAmount',
            field=models.PositiveIntegerField(default=1, verbose_name='Quantity'),
        ),
    ]