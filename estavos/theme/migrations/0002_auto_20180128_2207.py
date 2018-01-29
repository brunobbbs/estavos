# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='active',
            field=models.BooleanField(verbose_name='Ativo', default=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(verbose_name='Imagem', help_text='Use uma imagem com tamanho de 1600x575', upload_to='home/banners/'),
        ),
    ]
