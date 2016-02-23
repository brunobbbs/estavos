# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_inscription_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='classes',
            field=models.CharField(max_length=50, verbose_name='Turmas'),
        ),
    ]
