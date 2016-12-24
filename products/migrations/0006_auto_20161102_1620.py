# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20161102_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='iventory',
            new_name='inventory',
        ),
    ]
