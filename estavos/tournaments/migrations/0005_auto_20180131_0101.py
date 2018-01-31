# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_auto_20180130_2353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inscriptionprice',
            options={'ordering': ['limit_date']},
        ),
        migrations.RemoveField(
            model_name='inscriptionprice',
            name='half',
        ),
    ]
