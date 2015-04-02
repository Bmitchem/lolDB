# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0003_auto_20150402_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('group', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=528)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
