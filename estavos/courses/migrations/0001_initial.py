# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=150)),
                ('place', models.CharField(verbose_name='Local', max_length=100)),
                ('start_date', models.DateField(verbose_name='Data de início')),
                ('classes', models.CharField(verbose_name='Turmas', max_length=50)),
                ('is_active', models.BooleanField(verbose_name='Ativo?', default=False)),
                ('price', models.DecimalField(verbose_name='Preço', default=Decimal('449.70'), max_digits=6, decimal_places=2)),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
                'ordering': ('start_date',),
            },
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=150)),
                ('phone', models.CharField(verbose_name='Telefone', max_length=15)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
                ('student', models.CharField(verbose_name='Aluno', max_length=150)),
                ('birth', models.DateField(verbose_name='Data de nascimento')),
                ('created_at', models.DateTimeField(verbose_name='Inscrição realizada em', auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('course', models.ForeignKey(verbose_name='Curso', related_name='inscriptions', to='courses.Course')),
            ],
            options={
                'verbose_name': 'inscrição',
                'verbose_name_plural': 'inscrições',
                'ordering': ('-created_at',),
            },
        ),
    ]
