# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-29 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0018_prizes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prizes',
            new_name='Prize',
        ),
    ]
