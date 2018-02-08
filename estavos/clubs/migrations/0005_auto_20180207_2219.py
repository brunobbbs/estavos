# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_club_district'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubprice',
            old_name='price',
            new_name='value',
        ),
    ]
