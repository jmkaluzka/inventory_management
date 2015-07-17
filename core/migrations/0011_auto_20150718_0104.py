# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150718_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='model',
        ),
        migrations.RemoveField(
            model_name='device',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='device',
            name='production_year',
        ),
        migrations.AddField(
            model_name='device',
            name='device_name',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
    ]
