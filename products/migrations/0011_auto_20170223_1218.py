# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20170223_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
