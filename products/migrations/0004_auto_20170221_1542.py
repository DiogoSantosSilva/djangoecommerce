# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170221_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Subcategory',
            field=models.ForeignKey(related_name='default_subcategory', to='products.SubCategory', default='games'),
        ),
    ]
