# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150717_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelwithfilefield',
            old_name='docfile',
            new_name='file',
        ),
    ]
