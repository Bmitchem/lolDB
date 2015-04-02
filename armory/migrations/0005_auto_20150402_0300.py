# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0004_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.CharField(max_length=1024),
            preserve_default=True,
        ),
    ]
