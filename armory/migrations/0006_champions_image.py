# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0005_auto_20150416_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='champions',
            name='image',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
