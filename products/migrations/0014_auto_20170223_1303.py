# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20170223_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='products.SubCategory', chained_field='category', chained_model_field='category'),
        ),
    ]
