__author__ = 'bob'


def populate(json_file):
    MATCH_DATA = json.load(open(json_file))
    for match in MATCH_DATA.get('matches'):
        match_db, unused = models.MatchSummary.objects.get_or_create(matchId=match.get('matchId'),
                            region=match.get('region'),
                            platformId=match.get('platformId'),
                            matchCreation=match.get('matchDuration'),
                            matchDuration=match.get('matchDuration'),
                            queueType=match.get('queueType'),
                            season=match.get('season'),
                            matchVersion=match.get('matchVersion'),
                            mapId=match.get('mapId'),
                            matchMode=match.get('matchMode'),
                            matchType=match.get('matchType'),
                            )
        participants = match.get('participants')
        for participant in participants:
            p, unused = models.Participant.objects.get_or_create(teamId=participant.get('teamId'),
                                                 spell1Id=participant.get('spell1Id'),
                                                 spell2Id=participant.get('spell2Id'),
                                                 championId=participant.get('championId'),
                                                 highestAchievedSeasonTier=participant.get('highestAchievedSeasonTier'),
                                                 participantId=participant.get('participantId'),
                                                 )
            p.save()
            match_db.participants.add(p)
            match_db.save()
            stats = participant.get('stats')
            p_stats, unused = models.ParticipantStats.objects.get_or_create(
                winner=stats.get('winner'),
                champLevel=stats.get('champLevel'),
                item0=stats.get('item0'),
                item1=stats.get('item1'),
                item2=stats.get('item2'),
                item3=stats.get('item3'),
                item4=stats.get('item4'),
                item5=stats.get('item5'),
                item6=stats.get('item6'),
                kills=stats.get('kills'),
                doubleKills=stats.get('doubleKills'),
                tripleKills=stats.get('tripleKills'),
                quadraKills=stats.get('quadraKills'),
                pentaKills=stats.get('pentaKills'),
                largestKillingSpree=stats.get('largestKillingSpree'),
                deaths=stats.get('deaths'),
                assists=stats.get('assists'),
                totalDamageDealtToChampions=stats.get('totalDamageDealtToChampions'),
                totalDamageDealt=stats.get('totalDamageDealt'),
                largestCriticalStrike=stats.get('largestCriticalStrike'),
                totalHeal=stats.get('totalHeal'),
                minionsKilled=stats.get('minionsKilled'),
                neutralMinionsKilled=stats.get('neutralMinionsKilled'),
                neutralMinionsKilledTeamJungle=stats.get('neutralMinionsKilledTeamJungle'),
                neutralMinionsKilledEnemyJungle=stats.get('neutralMinionsKilledEnemyJungle'),
                goldEarned=stats.get('goldEarned'),
                goldSpent=stats.get('goldSpent'),
                combatPlayerScore=stats.get('combatPlayerScore'),
                objectivePlayerScore=stats.get('objectivePlayerScore'),
                totalPlayerScore=stats.get('totalPlayerScore'),
                totalScoreRank=stats.get('totalScoreRank'),
                magicDamageDealtToChampions=stats.get('magicDamageDealtToChampions'),
                physicalDamageDealtToChampions=stats.get('physicalDamageDealtToChampions'),
                trueDamageDealtToChampions=stats.get('trueDamageDealtToChampions'),
                visionWardsBoughtInGame=stats.get('visionWardsBoughtInGame'),
                sightWardsBoughtInGame=stats.get('sightWardsBoughtInGame'),
                magicDamageDealt=stats.get('magicDamageDealt'),
                physicalDamageDealt=stats.get('physicalDamageDealt'),
                magicDamageTaken=stats.get('magicDamageTaken'),
                physicalDamageTaken=stats.get('physicalDamageTaken'),
                trueDamageTaken=stats.get('trueDamageTaken'),
                firstBloodKill=stats.get('firstBloodKill'),
                firstBloodAssist=stats.get('firstBloodAssist'),
                firstTowerKill=stats.get('firstTowerKill'),
                firstTowerAssist=stats.get('firstTowerAssist'),
                firstInhibitorKill=stats.get('firstInhibitorKill'),
                firstInhibitorAssist=stats.get('firstInhibitorAssist'),
                inhibitorKills=stats.get('inhibitorKills'),
                towerKills=stats.get('towerKills'),
                wardsPlaced=stats.get('wardsPlaced'),
                wardsKilled=stats.get('wardsKilled'),
                largestMultiKill=stats.get('largestMultiKill'),
                killingSprees=stats.get('killingSprees'),
                totalUnitsHealed=stats.get('totalUnitsHealed'),
                totalTimeCrowdControlDealt=stats.get('totalTimeCrowdControlDealt'),
                )
            p_stats.participant = p.participantId
            p_stats.save()

if __name__=='__main__':
    import os
    import json
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RiotProject.settings")
    from armory import models
    print "Starting Population Script"
    import django
    import datetime
    from riot_api import RiotInterface
    ri = RiotInterface()
    django.setup()
    for i in range(1,9):
        starttime = datetime.datetime.now()
        print "uploading file: ", i
        populate('matches%s.json' % i)
        print "finished in ", datetime.datetime.now()-starttime

    print "updating champions"
    ri.update_champions()


