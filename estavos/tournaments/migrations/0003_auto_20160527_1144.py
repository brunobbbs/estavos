# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_inscription_confirmed'),
    ]

    def gen_uuid(apps, schema_editor):
        Inscription = apps.get_model("tournaments", "Inscription")
        for row in Inscription.objects.all():
            row.slug = uuid.uuid4().hex
            row.save()

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, max_length=32, verbose_name='Cod. Inscri\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.RunPython(gen_uuid),
        migrations.AlterField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True)
        ),
        migrations.AlterField(
            model_name='inscription',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Telefone', blank=True),
        ),
    ]
