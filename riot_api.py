__author__ = 'bob'
import requests
from django.conf import settings
from armory import models
import logging


class RiotInterface(object):

    def __init__(self):
        pass

    def upload_match_history(self, MATCH_DATA):
        for match in MATCH_DATA.get('matches'):
            match_db, unused = models.MatchSummary.objects.get_or_create(matchId=match.get('matchId'),
                                defaults={
                                "region":match.get('region'),
                                "platformId":match.get('platformId'),
                                "matchCreation":match.get('matchDuration'),
                                "matchDuration":match.get('matchDuration'),
                                "queueType":match.get('queueType'),
                                "season":match.get('season'),
                                "matchVersion":match.get('matchVersion'),
                                "mapId":match.get('mapId'),
                                "matchMode":match.get('matchMode'),
                                "matchType":match.get('matchType'),
                                }
                                )
            participants = match.get('participants')
            for participant in participants:
                p = models.Participant(teamId=participant.get('teamId'),
                                                     spell1Id=participant.get('spell1Id'),
                                                     spell2Id=participant.get('spell2Id'),
                                                     championId=participant.get('championId'),
                                                     highestAchievedSeasonTier=participant.get('highestAchievedSeasonTier'),
                                                     )
                p.save()
                match_db.participants.add(p)
                match_db.save()
                stats = participant.get('stats')
                p_stats = models.ParticipantStats(
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
                p_stats.participant = p
                p_stats.save()
                match_db.participants.add(p)
                match_db.save()


    def pull_current_games(self, SummonerID):
        resp = requests.get('https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/%s?api_key=%s'
                            % (SummonerID, settings.RIOT_API_KEY))
        if resp.status_code == 404:
            return "Not in Game"
        elif resp.status_code == 200:
            return resp
    def match_history(self, SummonerID):
        resp = requests.get('https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/%s?api_key=%s' %
                            (str(SummonerID), settings.RIOT_API_KEY))
        if resp.status_code == 200:
            return resp
        else:
            raise Exception

    def get_champions(self, free=None):
        if free:
            resp = requests.get('https://na.api.pvp.net/api/lol/na/v1.2/champion?freeToPlay=%s&api_key=%s' %
                                (str(free), settings.RIOT_API_KEY))
        else:
            resp = requests.get('https://na.api.pvp.net/api/lol/na/v1.2/champion?api_key=%s' % settings.RIOT_API_KEY)

        if resp.status_code == 200:
            return resp
        else:
            raise Exception

    def update_champions(self):
        champion_list = self.get_champions().json()
        for champion in champion_list['champions']:
            logging.info("updating champion: ", champion['id'])
            c, new = models.Champions.objects.get_or_create(id=champion['id'],
                                                            defaults={
                                                                'active':champion['active'],
                                                                'freeToPlay':champion['freeToPlay'],
                                                                'botMmEnabled':champion['botMmEnabled'],
                                                                'rankedPlayEnabled':champion['rankedPlayEnabled']
                                                            })
    def get_items(self):
        resp = requests.get('https://global.api.pvp.net/api/lol/static-data/na/v1.2/item?itemListData=inStore&api_key=%s'
                            % settings.RIOT_API_KEY)
        if resp.status_code == 200:
            return resp
        else:
            raise Exception

    def update_items(self):
        items = self.get_items().json()
        items_list = items.get('data')
        key_list = []
        for i in items_list:
            key_list.append(i)

        for key in key_list:
            print "Saving item: ", items.get('data')[key]['name']
            i, new = models.Items.objects.get_or_create(id=items.get('data')[key]['id'],
                                                        defaults={
                                                            'name':items.get('data')[key]['name'],
                                                            'group':items.get('data')[key].get('group',None),
                                                            'description':items.get('data')[key]['description'],
                                                            'plaintext':items.get('data')[key].get('plaintext', None)
                                                        })

    def summoner_id_pull(self, summonerId):
        resp = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/%d/recent?api_key=%s' %
                            (summonerId, settings.RIOT_API_KEY))

        if resp.status_code == 200:
            return resp
        else:
            raise Exception

    def import_summoner_id_from_pull(self, summonerId):
        resp = self.summoner_id_pull(summonerId).json()
        curr_summoners = len(models.Summoners.objects.all())
        for game in resp['games']:
            try:
                player_sets = game['fellowPlayers']
                for players in player_sets:
                    champ = models.Champions.objects.get(id=players['championId'])
                    summoner, trash = models.Summoners.objects.get_or_create(summonerId=players['summonerId'],
                                                              defaults={
                                                                'teamId':players['teamId'],
                                                              })
                    summoner.save()
                    summoner.champion.add(champ)
                    summoner.save()
            except KeyError:
                import sys
                sys.exit("You're out of API requests: ")

        print "Added %d Summoners" % (len(models.Summoners.objects.all()) - curr_summoners)


