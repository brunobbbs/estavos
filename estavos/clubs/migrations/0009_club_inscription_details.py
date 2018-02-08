# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_auto_20180207_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='inscription_details',
            field=mezzanine.core.fields.RichTextField(verbose_name='Como se inscrever', default=''),
            preserve_default=False,
        ),
    ]
