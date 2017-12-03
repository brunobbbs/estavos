# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0022_auto_20171129_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='url',
        ),
    ]
