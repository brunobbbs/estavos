# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='cover',
            field=models.ImageField(verbose_name='Capa da página', blank=True, null=True, upload_to='tournaments/cover/'),
        ),
    ]
