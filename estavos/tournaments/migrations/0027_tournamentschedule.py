# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0026_auto_20171203_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(verbose_name='Data')),
                ('hour', models.TimeField(verbose_name='Hora')),
                ('activity', models.CharField(verbose_name='Atividade', max_length=140)),
                ('tournament', models.ForeignKey(to='tournaments.Tournament')),
            ],
            options={
                'verbose_name': 'programação',
                'verbose_name_plural': 'programações',
            },
        ),
    ]
