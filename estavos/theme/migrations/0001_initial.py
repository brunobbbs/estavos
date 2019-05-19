# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Título', max_length=150)),
                ('description', models.CharField(verbose_name='Descrição', max_length=300, blank=True)),
                ('action_name', models.CharField(verbose_name='Nome do botão de ação', max_length=50)),
                ('target', models.URLField(verbose_name='Link do botão')),
                ('image', models.ImageField(verbose_name='Imagem', help_text='Use uma imagem com tamanho de 1600x575', upload_to='home/banners/')),
                ('active', models.BooleanField(verbose_name='Ativo', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=150)),
                ('site', models.URLField(verbose_name='Site', blank=True, null=True)),
                ('image', models.ImageField(verbose_name='Logo do parceiro', help_text='Use uma imagem com tamanho de 212x65', upload_to='home/partners/')),
                ('active', models.BooleanField(verbose_name='Ativo', default=True)),
            ],
        ),
    ]
