# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0014_tournament_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='short_description',
            field=models.CharField(verbose_name='Descrição curta', max_length=250, blank=True),
        ),
    ]
