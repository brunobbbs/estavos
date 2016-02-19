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
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('place', models.CharField(max_length=6, choices=[('ascade', 'N\xfacleo de Xadrez do clube ASCADE'), ('kumon', 'Kumon \xc1guas Claras - Avenida das Castanheiras')])),
                ('klass', models.CharField(max_length=8, choices=[('children', 'Crian\xe7as'), ('adults', 'Adultos')])),
                ('student', models.CharField(max_length=150)),
                ('birth', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
