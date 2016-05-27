# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='Confirmado?'),
        ),
    ]
