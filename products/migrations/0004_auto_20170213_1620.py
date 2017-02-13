# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170213_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfeatured',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='productfeatured',
            old_name='text_right',
            new_name='text_rigth',
        ),
        migrations.RemoveField(
            model_name='productfeatured',
            name='text_css_color',
        ),
    ]
