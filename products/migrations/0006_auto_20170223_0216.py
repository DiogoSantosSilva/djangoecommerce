# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170221_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='newcategory',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='newsubcategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='category', chained_field='category', default=1, to='products.SubCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=1, to='products.Category'),
            preserve_default=False,
        ),
    ]
