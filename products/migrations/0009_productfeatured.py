# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20161104_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('imagage', models.ImageField(upload_to=products.models.image_upload_to_featured)),
                ('title', models.CharField(null=True, blank=True, max_length=120)),
                ('description', models.CharField(null=True, blank=True, max_length=220)),
                ('text_rigth', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
