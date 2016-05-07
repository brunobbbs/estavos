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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('first_name', models.CharField(max_length=20, verbose_name='Seu primeiro nome', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'subscription',
                'verbose_name_plural': 'subscriptions',
            },
        ),
    ]
