# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_auto_20161228_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=120, choices=[('billing', 'Billing'), ('shipping', 'Shipping')])),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserCheckout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='guestcheckout',
            name='user',
        ),
        migrations.DeleteModel(
            name='GuestCheckout',
        ),
        migrations.AddField(
            model_name='useradress',
            name='user',
            field=models.ForeignKey(to='orders.UserCheckout'),
        ),
    ]
