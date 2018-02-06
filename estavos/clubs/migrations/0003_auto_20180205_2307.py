# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_club_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('klass', models.CharField(verbose_name='Turma', max_length=140)),
                ('date', models.DateField(verbose_name='Data')),
                ('hour', models.TimeField(verbose_name='Hora')),
            ],
            options={
                'verbose_name': 'turma',
                'verbose_name_plural': 'turmas',
            },
        ),
        migrations.CreateModel(
            name='ClubPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Identificador', max_length=50, help_text='Ex.: Mensal')),
                ('price', models.DecimalField(verbose_name='Valor mensalidade', default='190.00', max_digits=7, decimal_places=2)),
                ('active', models.BooleanField(verbose_name='Ativo?')),
                ('notes', models.TextField(verbose_name='Observações', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='address',
            field=models.CharField(verbose_name='Endereço', max_length=100, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='cover',
            field=models.ImageField(verbose_name='Capa da página', blank=True, null=True, help_text='Use uma imagem no tamanho 1170x500', upload_to='clubs/cover/'),
        ),
        migrations.AddField(
            model_name='club',
            name='google_maps',
            field=models.TextField(verbose_name='Mapa do local', blank=True, help_text='Insira um iframe do Google maps. Tamanho recomendado: 330x300'),
        ),
        migrations.AddField(
            model_name='club',
            name='inscription_link',
            field=models.URLField(verbose_name='Link para página de inscrição', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='phone',
            field=models.CharField(verbose_name='Telefone', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='short_description',
            field=models.CharField(verbose_name='Descrição curta', max_length=350, blank=True),
        ),
        migrations.AddField(
            model_name='clubprice',
            name='club',
            field=models.ForeignKey(related_name='prices', to='clubs.Club'),
        ),
        migrations.AddField(
            model_name='clubclass',
            name='club',
            field=models.ForeignKey(to='clubs.Club'),
        ),
    ]
