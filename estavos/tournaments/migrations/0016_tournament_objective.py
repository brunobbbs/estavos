# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-29 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0015_auto_20171128_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='objective',
            field=models.TextField(blank=True, verbose_name='Objetivos'),
        ),
    ]