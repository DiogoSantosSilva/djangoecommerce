# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_auto_20161227_1735'),
        ('orders', '0003_auto_20161229_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('shipping_total_price', models.DecimalField(max_digits=50, default=5.99, decimal_places=2)),
                ('order_total', models.DecimalField(max_digits=50, decimal_places=2)),
                ('billing_address', models.ForeignKey(related_name='billing_address', to='orders.UserAdress')),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('shipping_address', models.ForeignKey(related_name='shipping_address', to='orders.UserAdress')),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
