# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0003_auto_20150409_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summoners',
            name='dateAdded',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
