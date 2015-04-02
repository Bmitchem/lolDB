# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('freeToPlay', models.BooleanField(default=False)),
                ('botMmEnabled', models.BooleanField(default=False)),
                ('rankedPlayEnabled', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('group', models.CharField(max_length=256, null=True)),
                ('description', models.CharField(max_length=1024)),
                ('plaintext', models.CharField(max_length=1024, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MatchSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mapId', models.CharField(max_length=b'25')),
                ('matchCreation', models.IntegerField(default=0)),
                ('matchDuration', models.IntegerField(default=0)),
                ('matchId', models.IntegerField(default=0)),
                ('matchMode', models.CharField(max_length=256)),
                ('matchType', models.CharField(max_length=256)),
                ('matchVersion', models.CharField(max_length=256)),
                ('platformId', models.CharField(max_length=256)),
                ('queueType', models.CharField(max_length=75)),
                ('region', models.CharField(max_length=10)),
                ('season', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('championId', models.IntegerField(default=0)),
                ('highestAchievedSeasonTier', models.CharField(max_length=25)),
                ('spell1Id', models.IntegerField(default=0)),
                ('spell2Id', models.IntegerField(default=0)),
                ('teamId', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParticipantStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summonerName', models.CharField(max_length=30)),
                ('champLevel', models.IntegerField(default=0)),
                ('combatPlayerScore', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('doubleKills', models.IntegerField(default=0)),
                ('firstBloodAssist', models.BooleanField(default=False)),
                ('firstBloodKill', models.BooleanField(default=False)),
                ('firstInhibitorAssist', models.BooleanField(default=False)),
                ('firstInhibitorKill', models.BooleanField(default=False)),
                ('firstTowerAssist', models.BooleanField(default=False)),
                ('firstTowerKill', models.BooleanField(default=False)),
                ('goldEarned', models.IntegerField(default=0)),
                ('goldSpent', models.IntegerField(default=0)),
                ('inhibitorKills', models.IntegerField(default=0)),
                ('item0', models.IntegerField(default=0)),
                ('item1', models.IntegerField(default=0)),
                ('item2', models.IntegerField(default=0)),
                ('item3', models.IntegerField(default=0)),
                ('item4', models.IntegerField(default=0)),
                ('item5', models.IntegerField(default=0)),
                ('item6', models.IntegerField(default=0)),
                ('killingSprees', models.IntegerField(default=0)),
                ('kills', models.IntegerField(default=0)),
                ('largestCriticalStrike', models.IntegerField(default=0)),
                ('largestKillingSpree', models.IntegerField(default=0)),
                ('largestMultiKill', models.IntegerField(default=0)),
                ('magicDamageDealt', models.IntegerField(default=0)),
                ('magicDamageDealtToChampions', models.IntegerField(default=0)),
                ('magicDamageTaken', models.IntegerField(default=0)),
                ('minionsKilled', models.IntegerField(default=0)),
                ('neutralMinionsKilled', models.IntegerField(default=0)),
                ('neutralMinionsKilledEnemyJungle', models.IntegerField(default=0)),
                ('neutralMinionsKilledTeamJungle', models.IntegerField(default=0)),
                ('nodeCapture', models.IntegerField(null=True)),
                ('nodeCaptureAssist', models.IntegerField(null=True)),
                ('nodeNeutralize', models.IntegerField(null=True)),
                ('nodeNeutralizeAssist', models.IntegerField(null=True)),
                ('objectivePlayerScore', models.IntegerField(null=True)),
                ('pentaKills', models.IntegerField(default=0)),
                ('physicalDamageDealt', models.IntegerField(default=0)),
                ('physicalDamageDealtToChampions', models.IntegerField(default=0)),
                ('physicalDamageTaken', models.IntegerField(default=0)),
                ('quadraKills', models.IntegerField(default=0)),
                ('sightWardsBoughtInGame', models.IntegerField(default=0)),
                ('teamObjective', models.IntegerField(null=True)),
                ('totalDamageDealt', models.IntegerField(default=0)),
                ('totalDamageDealtToChampions', models.IntegerField(default=0)),
                ('totalDamageTaken', models.IntegerField(default=0)),
                ('totalHeal', models.IntegerField(default=0)),
                ('totalPlayerScore', models.IntegerField(default=0)),
                ('totalScoreRank', models.IntegerField(default=0)),
                ('totalTimeCrowdControlDealt', models.IntegerField(default=0)),
                ('totalUnitsHealed', models.IntegerField(default=0)),
                ('towerKills', models.IntegerField(default=0)),
                ('tripleKills', models.IntegerField(default=0)),
                ('trueDamageDealt', models.IntegerField(default=0)),
                ('trueDamageDealtToChampions', models.IntegerField(default=0)),
                ('trueDamageTaken', models.IntegerField(default=0)),
                ('visionWardsBoughtInGame', models.IntegerField(default=0)),
                ('wardsKilled', models.IntegerField(default=0)),
                ('wardsPlaced', models.IntegerField(default=0)),
                ('winner', models.IntegerField(default=0)),
                ('participant', models.OneToOneField(to='armory.Participant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Summoners',
            fields=[
                ('summonerId', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('teamId', models.IntegerField(default=0)),
                ('champion', models.ManyToManyField(to='armory.Champions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='matchsummary',
            name='participants',
            field=models.ManyToManyField(to='armory.Participant', null=True),
            preserve_default=True,
        ),
    ]
