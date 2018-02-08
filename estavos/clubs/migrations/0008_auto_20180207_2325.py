# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0007_club_howto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubClassTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_time', models.TimeField(verbose_name='Início')),
                ('end_time', models.TimeField(verbose_name='Fim')),
            ],
        ),
        migrations.RenameField(
            model_name='clubclass',
            old_name='klass',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='clubclass',
            name='date',
        ),
        migrations.RemoveField(
            model_name='clubclass',
            name='hour',
        ),
        migrations.AddField(
            model_name='clubclass',
            name='weekday',
            field=models.CharField(verbose_name='Dia(s) da semana', max_length=140, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clubclasstime',
            name='cclass',
            field=models.ForeignKey(related_name='schedules', to='clubs.ClubClass'),
        ),
    ]
