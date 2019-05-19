# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, unique=True)),
                ('is_active', models.BooleanField(verbose_name='is active', default=False)),
                ('first_name', models.CharField(verbose_name='Seu primeiro nome', max_length=20, blank=True)),
            ],
            options={
                'verbose_name': 'subscription',
                'verbose_name_plural': 'subscriptions',
                'abstract': False,
            },
        ),
    ]
