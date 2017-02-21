# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170221_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Subcategory',
            field=models.ForeignKey(related_name='default_subcategory', to='products.SubCategory'),
        ),
    ]
