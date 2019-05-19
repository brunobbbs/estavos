# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome do atleta', max_length=100)),
                ('birth', models.DateField(verbose_name='Data de nascimento')),
                ('id_lbx', models.CharField(verbose_name='ID LBX', max_length=7, blank=True)),
                ('id_fide', models.CharField(verbose_name='ID FIDE', max_length=10, blank=True, help_text='Opcional. Informe se tiver um ID FIDE.')),
                ('club', models.CharField(verbose_name='Escola/Clube', max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome do responsável', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(verbose_name='Telefone', max_length=15, blank=True)),
                ('confirmed', models.BooleanField(verbose_name='Confirmado?', default=False)),
                ('slug', models.SlugField(verbose_name='Cod. Inscrição', max_length=32, unique=True)),
                ('created', models.DateTimeField(verbose_name='Data/Hora inscrição', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InscriptionPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Identificador', max_length=50, help_text='Ex.: 1º Lote')),
                ('full', models.DecimalField(verbose_name='Valor da inteira', default='30.00', max_digits=7, decimal_places=2)),
                ('limit_date', models.DateTimeField(verbose_name='Válido para inscrições realizadas até')),
                ('active', models.BooleanField(verbose_name='Ativo?')),
                ('notes', models.TextField(verbose_name='Observações', blank=True)),
            ],
            options={
                'ordering': ['limit_date'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('paid', models.BooleanField(verbose_name='Pago?', default=False)),
                ('payment_type', models.CharField(verbose_name='Forma de pagamento', max_length=1, default='1', choices=[('1', 'PagSeguro'), ('2', 'Depósito bancário/Transferência'), ('3', 'Isenção')])),
                ('receipt', models.FileField(verbose_name='Recibo', blank=True, null=True, upload_to='payments/receipts/')),
                ('status', models.CharField(max_length=1, default='1', choices=[('1', 'Aguardando pagamento'), ('2', 'Em análise'), ('3', 'Paga'), ('4', 'Disponível'), ('5', 'Em disputa'), ('6', 'Devolvida'), ('7', 'Cancelada')])),
                ('transaction', models.CharField(max_length=150, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Nome do prêmio', max_length=100)),
                ('description', models.TextField(verbose_name='Descrição', blank=True)),
                ('icon', models.CharField(verbose_name='Font-awesome icon. Ex.: "fa-trophy"', max_length=15, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Nome do evento', max_length=100)),
                ('short_description', models.CharField(verbose_name='Descrição curta', max_length=250, blank=True)),
                ('description', models.TextField(verbose_name='Descrição', blank=True)),
                ('modality', models.CharField(verbose_name='Modalidade', max_length=7, default='rapid', choices=[('classic', 'Clássico'), ('rapid', 'Rápido'), ('blitz', 'Relâmpago')])),
                ('cover', models.ImageField(verbose_name='Capa da página', blank=True, null=True, help_text='Use uma imagem no tamanho 1170x500', upload_to='tournaments/cover/')),
                ('objective', models.TextField(verbose_name='Objetivos', blank=True)),
                ('start_date', models.DateTimeField(verbose_name='Início')),
                ('end_date', models.DateTimeField(verbose_name='Previsão de término')),
                ('inscriptions_date_limit', models.DateTimeField(verbose_name='Data limite para inscrições')),
                ('active', models.BooleanField(verbose_name='Ativo?')),
                ('place', models.CharField(verbose_name='Local', max_length=50)),
                ('google_maps', models.TextField(verbose_name='Mapa do local do evento', blank=True, help_text='Insira um iframe do Google maps. Tamanho recomendado: 330x300')),
                ('rule', models.URLField(verbose_name='Link para download do regulamento')),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(verbose_name='Valor da inscrição', default='25.00', max_digits=7, decimal_places=2)),
                ('chess_results', models.URLField(verbose_name='Link para o ChessResults', blank=True)),
                ('pairing', models.CharField(verbose_name='Sistema de disputa', max_length=30, blank=True, help_text='Ex.: Suíço em 6 rodadas.')),
                ('game_time', models.CharField(verbose_name='Tempo de reflexão', max_length=150, blank=True, help_text="Ex.: 60'K.O")),
                ('notes', models.TextField(verbose_name='Observações gerais', blank=True)),
                ('flyer', models.ImageField(verbose_name='Folder do evento', blank=True, null=True, upload_to='tournaments/flyers/')),
            ],
        ),
        migrations.CreateModel(
            name='TournamentSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(verbose_name='Data')),
                ('hour', models.TimeField(verbose_name='Hora')),
                ('activity', models.CharField(verbose_name='Atividade', max_length=140)),
                ('tournament', models.ForeignKey(to='tournaments.Tournament')),
            ],
            options={
                'verbose_name': 'programação',
                'verbose_name_plural': 'programações',
            },
        ),
        migrations.AddField(
            model_name='prize',
            name='tournament',
            field=models.ForeignKey(related_name='prizes', to='tournaments.Tournament'),
        ),
        migrations.AddField(
            model_name='inscriptionprice',
            name='tournament',
            field=models.ForeignKey(related_name='available_prices', to='tournaments.Tournament'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, related_name='inscription', to='tournaments.Payment'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='tournament',
            field=models.ForeignKey(related_name='inscriptions', to='tournaments.Tournament'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='inscription',
            field=models.ForeignKey(related_name='competitors', to='tournaments.Inscription'),
        ),
    ]
