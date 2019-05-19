# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='pages.Page')),
                ('name', models.CharField(verbose_name='Nome do clube', max_length=150)),
                ('short_description', models.CharField(verbose_name='Descrição curta', max_length=350, blank=True)),
                ('howto', mezzanine.core.fields.RichTextField(verbose_name='Como funciona')),
                ('city', models.CharField(verbose_name='Cidade', max_length=100)),
                ('district', models.CharField(verbose_name='Bairro', max_length=100)),
                ('address', models.CharField(verbose_name='Endereço', max_length=100)),
                ('phone', models.CharField(verbose_name='Telefone', max_length=200, blank=True)),
                ('cover', models.ImageField(verbose_name='Capa da página', blank=True, null=True, help_text='Use uma imagem no tamanho 1170x500', upload_to='clubs/cover/')),
                ('google_maps', models.TextField(verbose_name='Mapa do local', blank=True, help_text='Insira um iframe do Google maps. Tamanho recomendado: 330x300')),
                ('inscription_details', mezzanine.core.fields.RichTextField(verbose_name='Como se inscrever')),
                ('inscription_link', models.URLField(verbose_name='Link para página de inscrição', blank=True, null=True)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='ClubClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Turma', max_length=140)),
                ('weekday', models.CharField(verbose_name='Dia(s) da semana', max_length=140)),
                ('club', models.ForeignKey(related_name='classes', to='clubs.Club')),
            ],
            options={
                'verbose_name': 'turma',
                'verbose_name_plural': 'turmas',
            },
        ),
        migrations.CreateModel(
            name='ClubClassTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_time', models.TimeField(verbose_name='Início')),
                ('end_time', models.TimeField(verbose_name='Fim')),
                ('cclass', models.ForeignKey(related_name='schedules', to='clubs.ClubClass')),
            ],
        ),
        migrations.CreateModel(
            name='ClubPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Identificador', max_length=50, help_text='Ex.: Mensal')),
                ('value', models.DecimalField(verbose_name='Valor mensalidade', default='190.00', max_digits=7, decimal_places=2)),
                ('active', models.BooleanField(verbose_name='Ativo?')),
                ('notes', models.TextField(verbose_name='Observações', blank=True)),
                ('club', models.ForeignKey(related_name='prices', to='clubs.Club')),
            ],
        ),
    ]
