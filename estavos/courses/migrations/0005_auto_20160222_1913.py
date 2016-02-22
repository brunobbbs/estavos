# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20160222_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='klass',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='place',
        ),
        migrations.AlterField(
            model_name='course',
            name='classes',
            field=models.CharField(max_length=15, choices=[('children', 'Crian\xe7as'), ('adults', 'Adultos')]),
        ),
    ]
