# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_auto_20180130_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='google_maps',
            field=models.TextField(verbose_name='Mapa do local do evento', blank=True, help_text='Insira um iframe do Google maps. Tamanho recomendado: 330x300'),
        ),
    ]
