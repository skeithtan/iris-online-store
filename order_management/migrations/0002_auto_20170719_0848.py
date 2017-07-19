# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='approved',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('S', 'Shipped'), ('C', 'Cancelled')], default='P', max_length=2),
        ),
    ]