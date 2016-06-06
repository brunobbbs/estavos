# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0007_auto_20160530_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='id_fide',
            field=models.CharField(max_length=10, verbose_name='ID FIDE', blank=True),
        ),
    ]
