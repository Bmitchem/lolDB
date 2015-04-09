# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='championId',
            new_name='champion',
        ),
        migrations.AddField(
            model_name='participant',
            name='matchId',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
