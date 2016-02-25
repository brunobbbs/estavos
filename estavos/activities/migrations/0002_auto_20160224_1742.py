# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'atividade', 'verbose_name_plural': 'atividades'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AddField(
            model_name='activity',
            name='duration',
            field=models.IntegerField(default=1, verbose_name='Dura\xe7\xe3o'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(related_name='activities', verbose_name='Categoria', to='activities.Category'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.CharField(max_length=150, verbose_name='Descri\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='partner',
            field=models.ForeignKey(verbose_name='Parceiro', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='transport',
            field=models.DecimalField(verbose_name='Transporte', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='category',
            name='value',
            field=models.DecimalField(verbose_name='Valor', max_digits=7, decimal_places=2),
        ),
    ]
