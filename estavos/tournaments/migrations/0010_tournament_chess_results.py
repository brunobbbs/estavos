# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-27 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0009_auto_20170925_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='chess_results',
            field=models.URLField(blank=True, verbose_name='Link para o ChessResults'),
        ),
    ]