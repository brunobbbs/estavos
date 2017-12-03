# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0025_tournament_google_maps'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='flyer',
            field=models.ImageField(verbose_name='Folder do evento', blank=True, null=True, upload_to='tournaments/flyers/'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='notes',
            field=models.TextField(verbose_name='Observações gerais', blank=True),
        ),
    ]
