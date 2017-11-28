# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0011_auto_20171128_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscription',
            old_name='created_at',
            new_name='created',
        ),
    ]
