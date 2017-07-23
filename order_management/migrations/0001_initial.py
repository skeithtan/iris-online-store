# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entity_management', '0001_initial'),
        ('customer_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_slip', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(default=None, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_profile.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Processing'), ('S', 'Shipped'), ('C', 'Cancelled')], default='P', max_length=2)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_profile.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('parent_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_management.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entity_management.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField()),
                ('associated_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='associated_product', to='entity_management.Product')),
                ('root_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='root_product', to='entity_management.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_profile.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity_management.Product')),
            ],
        ),
        migrations.CreateModel(
            name='WaitlistCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity_management.Product')),
            ],
        ),
        migrations.AddField(
            model_name='customerpaymentdetails',
            name='parent_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_management.Order'),
        ),
    ]