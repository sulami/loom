# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_note'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('order',)},
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.RemoveField(
            model_name='note',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='order',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='order',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
    ]
