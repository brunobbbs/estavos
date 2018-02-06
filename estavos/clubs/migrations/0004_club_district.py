# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20180205_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='district',
            field=models.CharField(verbose_name='Bairro', max_length=100, default=''),
            preserve_default=False,
        ),
    ]
