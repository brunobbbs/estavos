# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to='users/', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
