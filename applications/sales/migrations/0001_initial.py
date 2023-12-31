# Generated by Django 5.0 on 2023-12-14 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_date', models.DateField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('pay', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('ticket', models.BooleanField(default=True)),
                ('detail', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clientee', to='clients.clients')),
            ],
            options={
                'verbose_name': 'Egreso',
                'verbose_name_plural': 'Egresos',
                'order_with_respect_to': 'shipping_date',
            },
        ),
        migrations.CreateModel(
            name='ProductosEgreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('delivered', models.BooleanField(default=True)),
                ('returned', models.BooleanField(default=False)),
                ('egress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.egress')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
            options={
                'verbose_name': 'Producto egreso',
                'verbose_name_plural': 'Productos egreso',
                'order_with_respect_to': 'created',
            },
        ),
    ]
