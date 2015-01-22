# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20150122_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
