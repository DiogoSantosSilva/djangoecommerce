# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20161227_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentagem',
            field=models.DecimalField(max_digits=50, default=0.085, decimal_places=2),
        ),
    ]
