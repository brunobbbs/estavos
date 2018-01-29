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
                ('image', models.ImageField(upload_to='home/banners/')),
            ],
        ),
    ]
