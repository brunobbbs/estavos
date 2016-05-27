# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_auto_20160527_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='description',
            field=models.TextField(verbose_name='Descri\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(unique=True, max_length=32, verbose_name='Cod. Inscri\xe7\xe3o'),
        ),
    ]
