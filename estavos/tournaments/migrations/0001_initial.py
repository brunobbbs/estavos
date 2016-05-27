# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('email', models.EmailField(max_length=254)),
                ('birth', models.DateField(verbose_name='Data de nascimento')),
                ('id_cbx', models.CharField(max_length=7, verbose_name='ID CBX')),
                ('id_fide', models.CharField(max_length=7, verbose_name='ID FIDE', blank=True)),
                ('phone', models.CharField(max_length=15, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Nome do evento')),
                ('start_date', models.DateField(verbose_name='Data de in\xedcio')),
                ('end_date', models.DateField(verbose_name='Data de t\xe9rmino')),
                ('inscriptions_date_limit', models.DateTimeField(verbose_name='Data limite para inscri\xe7\xf5es')),
                ('active', models.BooleanField(verbose_name='Ativo?')),
                ('place', models.CharField(max_length=50, verbose_name='Local')),
                ('url', models.URLField(verbose_name='Link da p\xe1gina do evento')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='tournament',
            field=models.ForeignKey(related_name='inscriptions', to='tournaments.Tournament'),
        ),
    ]
