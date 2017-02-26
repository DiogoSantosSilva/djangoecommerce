# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='created', max_length=120, choices=[('created', 'Created'), ('paid', 'Paid'), ('shippend', 'Shipped'), ('refunded', 'Refunded')]),
        ),
    ]
