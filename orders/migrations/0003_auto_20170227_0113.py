# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170225_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradress',
            name='type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], default='Billing', max_length=120),
        ),
    ]
