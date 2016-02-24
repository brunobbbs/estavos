# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('transport', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(to='activities.Category'),
        ),
        migrations.AddField(
            model_name='activity',
            name='partner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
