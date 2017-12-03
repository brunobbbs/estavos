# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0023_remove_tournament_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='game_time',
            field=models.CharField(verbose_name='Tempo de reflexão', max_length=150, blank=True, help_text="Ex.: 60'K.O"),
        ),
        migrations.AddField(
            model_name='tournament',
            name='modality',
            field=models.CharField(verbose_name='Modalidade', max_length=7, default='rapid', choices=[('classic', 'Clássico'), ('rapid', 'Rápido'), ('blitz', 'Relâmpago')]),
        ),
        migrations.AddField(
            model_name='tournament',
            name='pairing',
            field=models.CharField(verbose_name='Sistema de disputa', max_length=30, blank=True, help_text='Ex.: Suíço em 6 rodadas.'),
        ),
    ]
