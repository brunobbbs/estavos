# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='pages.Page')),
                ('name', models.CharField(verbose_name='Nome do clube', max_length=150)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
