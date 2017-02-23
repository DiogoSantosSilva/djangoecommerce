# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170221_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='Subcategory',
            field=models.ForeignKey(to='products.SubCategory', related_name='default_subcategory', default=1),
            preserve_default=False,
        ),
    ]
