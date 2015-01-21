# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 1, 22, 8, 31, 17, 488119, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='threads',
            field=models.ManyToManyField(to='campaigns.Thread', blank=True),
            preserve_default=True,
        ),
    ]
