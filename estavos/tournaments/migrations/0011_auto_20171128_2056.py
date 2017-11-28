# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0010_tournament_chess_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 22, 56, 45, 452079, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 22, 56, 58, 964325, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='receipt',
            field=models.FileField(verbose_name='Recibo', blank=True, null=True, upload_to='payments/receipts/'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
