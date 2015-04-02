# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0002_auto_20150402_0128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='champions',
            old_name='rankedPlayEnaaabled',
            new_name='rankedPlayEnabled',
        ),
    ]
