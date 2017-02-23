# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='Subcategory',
            field=models.ManyToManyField(related_name='default_subcategory', to='products.SubCategory'),
        ),
    ]
