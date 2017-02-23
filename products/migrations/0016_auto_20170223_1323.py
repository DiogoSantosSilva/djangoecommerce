# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20170223_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]
