# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity_management', '0005_product_is_active'),
        ('order_management', '0004_auto_20170719_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLineItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('parent_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_management.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entity_management.Product')),
            ],
        ),
    ]
