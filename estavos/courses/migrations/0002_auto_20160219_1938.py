# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='birth',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='klass',
            field=models.CharField(max_length=8, verbose_name='Turma', choices=[('children', 'Crian\xe7as'), ('adults', 'Adultos')]),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='place',
            field=models.CharField(max_length=6, verbose_name='Local', choices=[('kumon', 'Kumon \xc1guas Claras - Avenida das Castanheiras - In\xedcio 12/03/2016')]),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='student',
            field=models.CharField(max_length=150, verbose_name='Aluno'),
        ),
    ]
