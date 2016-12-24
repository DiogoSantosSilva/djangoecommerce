# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20161105_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfeatured',
            old_name='imagage',
            new_name='image',
        ),
    ]
