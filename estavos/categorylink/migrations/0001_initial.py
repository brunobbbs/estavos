# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryLink',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='pages.Page')),
                ('blog_category', models.ForeignKey(to='blog.BlogCategory')),
            ],
            options={
                'verbose_name': 'Category link',
                'verbose_name_plural': 'Category links',
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
