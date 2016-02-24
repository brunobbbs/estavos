# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import migrations, models
from estavos.courses.models import Inscription


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20160223_1341'),
    ]

    def gen_uuid(apps, schema_editor):
        for row in Inscription.objects.all():
            row.slug = uuid.uuid4().get_hex()
            row.save()

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(default=uuid.uuid4),
            preserve_default=True,
        ),
        migrations.RunPython(gen_uuid),

        migrations.AlterField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True)
        )
    ]
