# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170221_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(to='products.Category', related_name='category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Subcategory',
            field=models.ForeignKey(default=datetime.datetime(2017, 2, 21, 15, 34, 9, 216792, tzinfo=utc), related_name='default_subcategory', to='products.SubCategory'),
            preserve_default=False,
        ),
    ]
