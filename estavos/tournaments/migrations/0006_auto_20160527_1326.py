# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0005_tournament_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='url',
            field=models.URLField(null=True, verbose_name='Link da p\xe1gina do evento', blank=True),
        ),
    ]
