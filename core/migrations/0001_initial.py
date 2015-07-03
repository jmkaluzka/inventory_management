# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, auto_created=True, to='core.User')),
                ('password', models.CharField(max_length=50)),
            ],
            bases=('core.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, auto_created=True, to='core.User')),
                ('students_number', models.IntegerField(max_length=5)),
                ('remarks', models.TextField(max_length=300)),
            ],
            bases=('core.user',),
        ),
    ]
