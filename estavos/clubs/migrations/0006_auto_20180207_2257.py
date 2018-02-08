# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_auto_20180207_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubclass',
            name='club',
            field=models.ForeignKey(related_name='classes', to='clubs.Club'),
        ),
    ]
