# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20160222_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('place', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('classes', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('start_date',),
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
            },
        ),
        migrations.AlterField(
            model_name='inscription',
            name='klass',
            field=models.CharField(max_length=8, verbose_name='Turma', choices=[('children', 'Crian\xe7as')]),
        ),
    ]
