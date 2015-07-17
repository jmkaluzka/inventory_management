# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_modelwithfilefield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelwithfilefield',
            name='name',
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.CharField(max_length=50, default='model'),
        ),
        migrations.AddField(
            model_name='modelwithfilefield',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d', blank=True),
        ),
    ]
