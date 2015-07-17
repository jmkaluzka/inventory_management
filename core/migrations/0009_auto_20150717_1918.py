# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150717_1852'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ModelWithFileField',
            new_name='Document',
        ),
    ]
