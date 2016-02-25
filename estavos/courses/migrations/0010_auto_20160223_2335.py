# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_inscription_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(default=Decimal('449.70'), verbose_name='Pre\xe7o', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
