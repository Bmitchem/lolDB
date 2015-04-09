# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0002_auto_20150403_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='championId',
            field=models.ManyToManyField(to='armory.Champions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='fellowPlayers',
            field=models.ManyToManyField(to='armory.Participant'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='stats',
            field=models.ManyToManyField(to='armory.ParticipantStats'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matchsummary',
            name='participants',
            field=models.ManyToManyField(to='armory.Summoners'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='summoners',
            name='champion',
            field=models.ManyToManyField(to='armory.Champions'),
            preserve_default=True,
        ),
    ]
