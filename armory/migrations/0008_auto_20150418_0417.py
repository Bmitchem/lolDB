# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0007_auto_20150418_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champions',
            name='aram_winrate',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='champions',
            name='dominion_winrate',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='champions',
            name='popularity',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='champions',
            name='rift_winrate',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='champions',
            name='treeline_winrate',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
            preserve_default=True,
        ),
    ]
