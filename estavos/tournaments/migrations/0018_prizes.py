# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-29 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0017_tournament_rule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nome do evento')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('icon', models.CharField(blank=True, max_length=15, verbose_name='Font-awesome icon. Ex.: "fa-trophy"')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prizes', to='tournaments.Tournament')),
            ],
        ),
    ]