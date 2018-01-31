# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_tournament_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='cover',
            field=models.ImageField(verbose_name='Capa da página', blank=True, null=True, help_text='Use uma imagem no tamanho 1170x500', upload_to='tournaments/cover/'),
        ),
    ]
