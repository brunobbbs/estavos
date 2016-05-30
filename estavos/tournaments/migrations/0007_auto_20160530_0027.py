# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0006_auto_20160527_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='end_date',
            field=models.DateTimeField(verbose_name='Previs\xe3o de t\xe9rmino'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_date',
            field=models.DateTimeField(verbose_name='In\xedcio'),
        ),
    ]
