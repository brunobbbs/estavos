# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0008_auto_20160605_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome do atleta', max_length=100)),
                ('birth', models.DateField(verbose_name='Data de nascimento')),
                ('id_lbx', models.CharField(verbose_name='ID LBX', max_length=7)),
                ('id_fide', models.CharField(verbose_name='ID FIDE', max_length=10, blank=True, help_text='Opcional. Informe se tiver um ID FIDE.')),
                ('club', models.CharField(verbose_name='Escola/Clube', max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('paid', models.BooleanField(verbose_name='Pago?', default=False)),
                ('payment_type', models.CharField(verbose_name='Forma de pagamento', max_length=1, default='1', choices=[('1', 'PagSeguro'), ('2', 'Depósito bancário/Transferência'), ('3', 'Isenção')])),
                ('receipt', models.FileField(verbose_name='Recibo', blank=True, null=True, upload_to='tournaments/receipts/')),
                ('status', models.CharField(max_length=1, default='1', choices=[('1', 'Aguardando pagamento'), ('2', 'Em análise'), ('3', 'Paga'), ('4', 'Disponível'), ('5', 'Em disputa'), ('6', 'Devolvida'), ('7', 'Cancelada')])),
                ('transaction', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='id_cbx',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='id_fide',
        ),
        migrations.AddField(
            model_name='inscription',
            name='created_at',
            field=models.DateTimeField(verbose_name='Data/Hora inscrição', default=datetime.datetime(2017, 9, 26, 0, 46, 17, 822330, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='price',
            field=models.DecimalField(verbose_name='Valor da inscrição', default='20.00', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='name',
            field=models.CharField(verbose_name='Nome do responsável', max_length=100),
        ),
        migrations.AddField(
            model_name='competitor',
            name='inscription',
            field=models.ForeignKey(related_name='competitors', to='tournaments.Inscription'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, related_name='inscription', to='tournaments.Payment'),
        ),
    ]
