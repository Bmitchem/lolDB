# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0005_auto_20150402_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='plaintext',
            field=models.CharField(max_length=1024, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='items',
            name='group',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]
