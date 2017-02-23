# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170221_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='subcategory', default=1, to='products.SubCategory', chained_model_field='category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='Category',
            field=models.ForeignKey(to='products.Category', related_name='new_subcategory'),
        ),
    ]
