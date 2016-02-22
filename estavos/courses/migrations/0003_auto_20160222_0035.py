# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160219_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inscription',
            options={'ordering': ('-created_at',), 'verbose_name': 'inscri\xe7\xe3o', 'verbose_name_plural': 'inscri\xe7\xf5es'},
        ),
        migrations.AlterField(
            model_name='inscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Inscri\xe7\xe3o realizada em'),
        ),
    ]
