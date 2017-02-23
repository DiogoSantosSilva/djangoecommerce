# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170221_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='newcategory',
            field=models.ForeignKey(default=1, to='products.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='newsubcategory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='category', default=1, chained_field='newcategory', to='products.SubCategory'),
            preserve_default=False,
        ),
    ]
