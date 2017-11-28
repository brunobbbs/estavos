# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0012_auto_20171128_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='id_lbx',
            field=models.CharField(verbose_name='ID LBX', max_length=7, blank=True),
        ),
    ]
