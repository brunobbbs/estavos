# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_inscription_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
