# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0024_auto_20171203_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='google_maps',
            field=models.TextField(verbose_name='Mapa do local do evento', blank=True, help_text='Insira um iframe do Google maps'),
        ),
    ]
