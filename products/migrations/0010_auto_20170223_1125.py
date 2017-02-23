# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170223_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_model_field='category', to='products.SubCategory', chained_field='category'),
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
