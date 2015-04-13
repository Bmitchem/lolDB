# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0002_champions_winrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantstats',
            name='championId',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
