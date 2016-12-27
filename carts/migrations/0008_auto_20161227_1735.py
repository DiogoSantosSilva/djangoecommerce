# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_cart_tax_percentagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='tax_percentagem',
            new_name='tax_percentage',
        ),
    ]
