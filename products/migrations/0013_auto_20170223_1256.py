# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20170223_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(default=1, chained_model_field='category', chained_field='category', to='products.SubCategory'),
            preserve_default=False,
        ),
    ]
