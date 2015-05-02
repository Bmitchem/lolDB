# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('armory', '0004_participantstats_summonerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='fellowPlayers',
            field=models.ManyToManyField(to='armory.Participant', db_index=True),
            preserve_default=True,
        ),
    ]
