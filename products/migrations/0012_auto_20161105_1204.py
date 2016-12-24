# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_productfeatured_make_image_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeatured',
            name='make_image_background',
            field=models.BooleanField(default=False),
        ),
    ]
