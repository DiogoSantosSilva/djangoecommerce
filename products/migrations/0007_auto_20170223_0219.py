# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170223_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_model_field='category', to='products.SubCategory', chained_field='category'),
        ),
    ]
