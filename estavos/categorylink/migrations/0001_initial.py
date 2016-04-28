# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('blog', '0002_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryLink',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('blog_category', models.ForeignKey(to='blog.BlogCategory')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Category link',
                'verbose_name_plural': 'Category links',
            },
            bases=('pages.page',),
        ),
    ]
