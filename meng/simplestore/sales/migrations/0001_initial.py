# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-08 18:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0015_auto_20171208_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salesperson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(choices=[('S', 'Saler'), ('M', 'Store_manager'), ('R', 'Region_manager')], max_length=1)),
                ('salary', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.PositiveIntegerField()),
                ('store_name', models.CharField(max_length=255)),
                ('region_name', models.CharField(choices=[('NE', 'Northeast'), ('SE', 'Southeast'), ('MW', 'Midwest'), ('SW', 'Southwest'), ('W', 'West')], max_length=2)),
                ('aid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='checkout.Address')),
            ],
        ),
        migrations.AddField(
            model_name='salesperson',
            name='store_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sales.Store'),
        ),
    ]