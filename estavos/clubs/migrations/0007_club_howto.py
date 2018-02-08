# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_auto_20180207_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='howto',
            field=mezzanine.core.fields.RichTextField(verbose_name='Como funciona', default=''),
            preserve_default=False,
        ),
    ]
