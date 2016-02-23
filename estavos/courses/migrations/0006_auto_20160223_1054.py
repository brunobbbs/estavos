# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20160222_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='classes',
            field=models.CharField(max_length=15, verbose_name='Turmas', choices=[('children', 'Crian\xe7as'), ('adults', 'Adultos')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='course',
            name='place',
            field=models.CharField(max_length=100, verbose_name='Local'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(verbose_name='Data de in\xedcio'),
        ),
    ]
