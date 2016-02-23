# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20160223_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='course',
            field=models.ForeignKey(related_name='inscriptions', default=1, verbose_name='Curso', to='courses.Course'),
            preserve_default=False,
        ),
    ]
