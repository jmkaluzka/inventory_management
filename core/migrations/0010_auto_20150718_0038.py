# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150717_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='file',
        ),
        migrations.AddField(
            model_name='document',
            name='path',
            field=models.FileField(upload_to='documents', blank=True),
        ),
    ]
