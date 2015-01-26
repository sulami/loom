# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_auto_20150125_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='campaign',
        ),
        migrations.RemoveField(
            model_name='event',
            name='threads',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
