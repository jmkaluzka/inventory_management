# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='production_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='remarks',
            field=models.TextField(),
        ),
    ]
