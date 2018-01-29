# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_auto_20180128_2207'),
    ]

    operations = [
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
