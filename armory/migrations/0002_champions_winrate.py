# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('armory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='champions',
            name='winrate',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
