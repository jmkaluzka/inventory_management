# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150717_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelwithfilefield',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='modelwithfilefield',
            name='file',
            field=models.FileField(blank=True, upload_to='csvs'),
        ),
    ]
