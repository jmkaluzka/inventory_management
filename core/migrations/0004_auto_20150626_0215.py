# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150626_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='remarks',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='students_number',
            field=models.IntegerField(),
        ),
    ]
