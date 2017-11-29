# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0013_auto_20171128_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='short_description',
            field=models.TextField(verbose_name='Descrição', blank=True),
        ),
    ]
