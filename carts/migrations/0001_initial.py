# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(default='created', choices=[('created', 'Created'), ('completed', 'Completed')], max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tax_percentage', models.DecimalField(default=0.085, max_digits=50, decimal_places=2)),
                ('tax_total', models.DecimalField(default=25.0, max_digits=50, decimal_places=2)),
                ('subtotal', models.DecimalField(default=25.0, max_digits=50, decimal_places=2)),
                ('total', models.DecimalField(default=25.0, max_digits=50, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('line_item_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('item', models.ForeignKey(to='products.Variation')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='carts.CartItem', to='products.Variation'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
