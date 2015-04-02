# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champions',
            name='rankedPlayEnabled',
        ),
        migrations.AddField(
            model_name='champions',
            name='rankedPlayEnaaabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
