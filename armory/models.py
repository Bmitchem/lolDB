__author__ = 'bob'
from django.db import models
import numpy

class Participant(models.Model):
    summonerId =  models.IntegerField(primary_key=True)
    champion = models.IntegerField(default=0)
    highestAchievedSeasonTier = models.CharField(max_length=25, null=True)
    spell1Id = models.IntegerField(default=0)
    spell2Id = models.IntegerField(default=0)
    teamId = models.IntegerField(default=0)
    matchId = models.IntegerField(default=0)


class ParticipantStats(models.Model):
    participant = models.ManyToManyField(Participant)
    summonerName = models.CharField(max_length=30, null=True)
    champLevel = models.IntegerField(default=0)
    combatPlayerScore = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    doubleKills = models.IntegerField(default=0)
    firstBloodAssist = models.BooleanField(default=False)
    firstBloodKill = models.BooleanField(default=False)
    firstInhibitorAssist = models.BooleanField(default=False)
    firstInhibitorKill = models.BooleanField(default=False)
    firstTowerAssist = models.BooleanField(default=False)
    firstTowerKill = models.BooleanField(default=False)
    goldEarned = models.IntegerField(default=0)
    goldSpent = models.IntegerField(default=0)
    inhibitorKills = models.IntegerField(default=0)
    item0 = models.IntegerField(default=0)
    item1 = models.IntegerField(default=0)
    item2 = models.IntegerField(default=0)
    item3 = models.IntegerField(default=0)
    item4 = models.IntegerField(default=0)
    item5 = models.IntegerField(default=0)
    item6 = models.IntegerField(default=0)
    killingSprees = models.IntegerField(default=0)
    kills = models.IntegerField(default=0)
    largestCriticalStrike = models.IntegerField(default=0)
    largestKillingSpree = models.IntegerField(default=0)
    largestMultiKill = models.IntegerField(default=0)
    magicDamageDealt = models.IntegerField(default=0)
    magicDamageDealtToChampions = models.IntegerField(default=0)
    magicDamageTaken = models.IntegerField(default=0)
    minionsKilled = models.IntegerField(default=0)
    neutralMinionsKilled = models.IntegerField(default=0)
    neutralMinionsKilledEnemyJungle = models.IntegerField(default=0)
    neutralMinionsKilledTeamJungle = models.IntegerField(default=0)
    nodeCapture = models.IntegerField(null=True)
    nodeCaptureAssist = models.IntegerField(null=True)
    nodeNeutralize = models.IntegerField(null=True)
    nodeNeutralizeAssist = models.IntegerField(null=True)
    objectivePlayerScore = models.IntegerField(null=True)
    pentaKills= models.IntegerField(default=0)
    physicalDamageDealt = models.IntegerField(default=0)
    physicalDamageDealtToChampions = models.IntegerField(default=0)
    physicalDamageTaken= models.IntegerField(default=0)
    quadraKills = models.IntegerField(default=0)
    sightWardsBoughtInGame = models.IntegerField(default=0)
    teamObjective = models.IntegerField(null=True)
    totalDamageDealt= models.IntegerField(default=0)
    totalDamageDealtToChampions = models.IntegerField(default=0)
    totalDamageTaken = models.IntegerField(default=0)
    totalHeal = models.IntegerField(default=0)
    totalPlayerScore = models.IntegerField(default=0)
    totalScoreRank = models.IntegerField(default=0)
    totalTimeCrowdControlDealt = models.IntegerField(default=0)
    totalUnitsHealed = models.IntegerField(default=0)
    towerKills = models.IntegerField(default=0)
    tripleKills = models.IntegerField(default=0)
    trueDamageDealt = models.IntegerField(default=0)
    trueDamageDealtToChampions = models.IntegerField(default=0)
    trueDamageTaken = models.IntegerField(default=0)
    visionWardsBoughtInGame = models.IntegerField(default=0)
    wardsKilled = models.IntegerField(default=0)
    wardsPlaced = models.IntegerField(default=0)
    winner = models.IntegerField(default=0)
    turretsKilled = models.IntegerField(default=0, null=True)
    playerPosition = models.IntegerField(default=0, null=True)
    playerRole = models.IntegerField(default=0, null=True)
    timePlayed = models.IntegerField(default=0, null=True)
    team = models.IntegerField(default=0, null=True)

class ChampionSkins(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    num = models.IntegerField(default=0)
    
class ChampionTags(models.Model):
    tag = models.CharField(max_length=56)
    
class ChampionStats(models.Model):
    championId = models.IntegerField(primary_key=True)
    armor = models.IntegerField(default=0)
    armorperlevel = models.IntegerField(default=0)
    attackdamage = models.IntegerField(default=0)
    attackdamageperlevel = models.IntegerField(default=0)
    attackrange = models.IntegerField(default=0)
    attackspeedoffset = models.IntegerField(default=0)
    attackspeedperlevel = models.IntegerField(default=0)
    crit = models.IntegerField(default=0)
    critperlevel = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    hpperlevel = models.IntegerField(default=0)
    hpregen = models.IntegerField(default=0)
    hpregenperlevel = models.IntegerField(default=0)
    movespeed = models.IntegerField(default=0)
    mp = models.IntegerField(default=0)
    mpperlevel = models.IntegerField(default=0)
    mpregen = models.IntegerField(default=0)
    mpregenperlevel = models.IntegerField(default=0)
    spellblock = models.IntegerField(default=0)
    spellblockperlevel = models.IntegerField(default=0)


class Champions(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.NullBooleanField(default=True, null=True)
    freeToPlay = models.NullBooleanField(default=False, null=True)
    botMmEnabled = models.NullBooleanField(default=False, null=True)
    rankedPlayEnabled = models.NullBooleanField(default=False, null=True)
    name = models.CharField(max_length=256)
    skins = models.ManyToManyField(ChampionSkins)
    tag = models.ManyToManyField(ChampionTags)
    stats = models.ManyToManyField(ChampionStats)

    @property
    def winrate(self):
        games = []
        player_stats = ParticipantStats.objects.all()
        for ps in player_stats:
            player = ps.participant.all()[0]
            if ps.winner:

                if player.champion == self.id:
                    games.append(ps.winner)
            else:
                if player.champion == self.id:
                    games.append(ps.winner)
        if games:
            return numpy.mean(games) * 100
        else:
            return "Not yet Recorded"



class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    group = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=1024)
    plaintext = models.CharField(max_length=1024, null=True)

class Summoners(models.Model):
    summonerId = models.IntegerField(default=0, primary_key=True)
    teamId = models.IntegerField(default=0, null=True)
    champion = models.ManyToManyField(Champions)
    dateAdded = models.DateTimeField(null=True)

class Game(models.Model):
    summonerId=models.IntegerField(default=0)
    gameId=models.IntegerField(primary_key=True)
    gameMode=models.CharField(max_length=50, null=False)
    gameType=models.CharField(max_length=50)
    mapId=models.IntegerField(default=0)
    championId=models.ManyToManyField(Champions)
    spell1=models.IntegerField(default=0)
    spell2=models.IntegerField(default=0)
    fellowPlayers=models.ManyToManyField(Participant)
    ipEarned=models.IntegerField(default=0)
    stats=models.ManyToManyField(ParticipantStats)
    matchCreation=models.DateTimeField()


class MatchSummary(models.Model):
    mapId = models.CharField(max_length="25")
    matchCreation = models.IntegerField(default=0)
    matchDuration = models.IntegerField(default=0)
    matchId = models.IntegerField(default=0)
    matchMode = models.CharField(max_length=256)
    matchType = models.CharField(max_length=256)
    matchVersion = models.CharField(max_length=256)
    participants = models.ManyToManyField(Summoners)
    platformId = models.CharField(max_length=256)
    queueType = models.CharField(max_length=75)
    region = models.CharField(max_length=10)
    season = models.CharField(max_length=25)