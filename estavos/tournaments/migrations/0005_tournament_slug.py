# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from estavos.tournaments.models import Tournament
from estavos.utils.slug import unique_slugify
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_auto_20160527_1150'),
    ]

    def auto_slug(apps, schema_editor):
        for row in Tournament.objects.all():
            row.slug = unique_slugify(row, row.title)
            row.save()

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(default=uuid.uuid4),
            preserve_default=True,
        ),
        migrations.RunPython(auto_slug),
        migrations.AlterField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True)
        )
    ]
