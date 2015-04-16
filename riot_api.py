__author__ = 'bob'
import requests
from django.conf import settings
from armory import models
import logging
from pprint import pprint


class RiotInterface(object):
    def __init__(self):
        pass

    def upload_match_history(self, MATCH_DATA):
        for match in MATCH_DATA.get('matches'):
            match_db, unused = models.MatchSummary.objects.get_or_create(matchId=match.get('matchId'),
                                                                         defaults={
                                                                             "region": match.get('region'),
                                                                             "platformId": match.get('platformId'),
                                                                             "matchCreation": match.get(
                                                                                 'matchDuration'),
                                                                             "matchDuration": match.get(
                                                                                 'matchDuration'),
                                                                             "queueType": match.get('queueType'),
                                                                             "season": match.get('season'),
                                                                             "matchVersion": match.get('matchVersion'),
                                                                             "mapId": match.get('mapId'),
                                                                             "matchMode": match.get('matchMode'),
                                                                             "matchType": match.get('matchType'),
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

    def update_free_champions(self):
        from django.core.exceptions import ObjectDoesNotExist
        champion_list=self.get_champions().json()
        for champion in champion_list['champions']:
            try:
                champ = models.Champions.objects.get(id=champion['id'])
                champ.freeToPlay = champion['freeToPlay']
                champ.save()
                if champion['freeToPlay']:
                    print "%s is free this week! " % champ.name
            except ObjectDoesNotExist:
                print "shit's broke"
                continue

    def update_champions(self):
        import json

        champion_list = json.load(open('champion_detail.json'))
        champion_keys = champion_list['data'].keys()

        for key in champion_keys:
            champion = champion_list['data'].get(key)
            print("processing champion: ", champion.get('name'))

            c, new = models.Champions.objects.get_or_create(id=champion.get('id'),
                                                       defaults={
                                                           'name': champion.get('name'),
                                                       })

            c.image = champion.get('image').get('full')
            c.save()
            stats_info = champion['stats']
            stats = models.ChampionStats.objects.get_or_create(championId=champion.get('id'),
                                                               defaults={
                                                                   "armor": stats_info.get('armor'),
                                                                   "armorperlevel": stats_info.get('armorperlevel'),
                                                                   "attackdamage": stats_info.get('attackdamage'),
                                                                   "attackdamageperlevel": stats_info.get(
                                                                       'attackdamageperlevel'),
                                                                   "attackrange": stats_info.get('attackrange'),
                                                                   "attackspeedoffset": stats_info.get(
                                                                       'attackspeedoffset'),
                                                                   "attackspeedperlevel": stats_info.get(
                                                                       'attackspeedperlevel'),
                                                                   "crit": stats_info.get('crit'),
                                                                   "critperlevel": stats_info.get('critperlevel'),
                                                                   "hp": stats_info.get('hp'),
                                                                   "hpperlevel": stats_info.get('hpperlevel'),
                                                                   "hpregen": stats_info.get('hpregen'),
                                                                   "hpregenperlevel": stats_info.get('hpregenperlevel'),
                                                                   "movespeed": stats_info.get('movespeed'),
                                                                   "mp": stats_info.get('mp'),
                                                                   "mpperlevel": stats_info.get('mpperlevel'),
                                                                   "mpregen": stats_info.get('mpregen'),
                                                                   "mpregenperlevel": stats_info.get('mpregenperlevel'),
                                                                   "spellblock": stats_info.get('spellblock'),
                                                                   "spellblockperlevel": stats_info.get(
                                                                       'spellblockperlevel'),
                                                               })[0]

            c.stats.add(stats)


            for skin in champion.get('skins'):
                new_skin = models.ChampionSkins.objects.get_or_create(id=skin.get('id'),
                                                                            defaults={
                                                                                'name': skin.get('name'),
                                                                                'num': skin.get('num'),
                                                                            }
                                                                    )[0]

                c.skins.add(new_skin)

            for tag in champion.get('tags'):
                new_tag = models.ChampionTags.objects.get_or_create(tag=tag)[0]

                c.tag.add(new_tag)

    def get_items(self):
        resp = requests.get(
            'https://global.api.pvp.net/api/lol/static-data/na/v1.2/item?itemListData=inStore&api_key=%s'
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
                                                            'name': items.get('data')[key]['name'],
                                                            'group': items.get('data')[key].get('group', None),
                                                            'description': items.get('data')[key]['description'],
                                                            'plaintext': items.get('data')[key].get('plaintext', None)
                                                        })

    def qsummoner_id_pull(self, summonerId):
        resp = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/%d/recent?api_key=%s' %
                            (summonerId, settings.RIOT_API_KEY))

        if resp.status_code == 200:
            return resp
        else:
            raise Exception

    def import_summoner_id_from_pull(self, summonerId):
        from datetime import datetime
        resp = self.summoner_id_pull(summonerId).json()
        # fd = open('starting_match_history.json', 'w+')
        # import json

        # resp = json.load(open('starting_match_history.json'))

        # pprint(resp)
        curr_summoners = len(models.Summoners.objects.all())
        curr_games = len(models.Game.objects.all())
        for game in resp['games']:
            try:

                champ = models.Champions.objects.get(id=game['championId'])
                new_match, new = models.Game.objects.get_or_create(gameId=game['gameId'],
                                                                     defaults={
                                                                         'mapId': game['mapId'],
                                                                         'matchCreation': datetime.fromtimestamp(game['createDate'] / 1000.0),
                                                                         'ipEarned': game['ipEarned'],
                                                                         'summonerId': resp['summonerId'],
                                                                         'spell1': game['spell1'],
                                                                         'spell2': game['spell2'],

                                                                     })

                new_match.gameType=game['gameType']
                new_match.gameMode=game['gameMode']
                new_match.save()

                new_match.championId.add(champ)
                if new:
                    print "Saving a new match! It was a: %s type game" % game['gameMode']

                player = models.Participant.objects.get_or_create(summonerId=summonerId,
                                                                  defaults={
                                                                    'spell1Id':game['spell1'],
                                                                    'spell2Id':game['spell2'],
                                                                    'teamId':game['teamId'],
                                                                    'matchId':game['gameId'],

                                                                  })[0]
                new_match.fellowPlayers.add(player)
                player_sets = game['fellowPlayers']
                for players in player_sets:
                    champ = models.Champions.objects.get(id=players['championId'])
                    participant, trash = models.Participant.objects.get_or_create(summonerId=players['summonerId'],
                                                                             defaults={
                                                                                 'teamId': players['teamId'],
                                                                             })
                    participant.champion = champ.id
                    participant.save()
                    summoner = models.Summoners.objects.get_or_create(summonerId=players['summonerId'],
                                                                      defaults={
                                                                                 'teamId': players['teamId'],
                                                                             }
                                                                      )[0]

                    summoner.champion.add(champ)
                    summoner.save()
                    new_match.fellowPlayers.add(participant)
                    new_match.championId.add(champ)
                    new_match.save()

                stats = game['stats']
                new_stats, trash = models.ParticipantStats.objects.get_or_create(
                    summonerId=players['summonerId'],
                    champLevel=stats.get('level', 0),
                    goldEarned=stats.get('goldEarned', 0),
                    deaths=stats.get('numDeaths', 0),
                    turretsKilled=stats.get('turretsKilled', 0),
                    kills=stats.get('championsKilled', 0),
                    goldSpent=stats.get('goldSpent', 0),
                    totalDamageDealt=stats.get('totalDamageDealt', 0),
                    totalDamageTaken=stats.get('totalDamageTaken', 0),
                    doubleKills=stats.get('doubleKills', 0),
                    tripleKills=stats.get('tripleKills', 0),
                    killingSprees=stats.get('killingSprees', 0),
                    largestKillingSpree=stats.get('largestKillingSpree', 0),
                    team=stats.get('team', 0),
                    winner=stats.get('win', 0),
                    neutralMinionsKilled=stats.get('neutralMinionsKilled', 0),
                    largestMultiKill=stats.get('largestMultiKill', 0),
                    physicalDamageDealt=stats.get('physicalDamageDealtPlayer', 0),
                    magicDamageDealt=stats.get('magicDamageDealtPlayer', 0),
                    physicalDamageTaken=stats.get('physicalDamageTaken', 0),
                    magicDamageTaken=stats.get('magicDamageTaken', 0),
                    timePlayed=stats.get('timePlayed', 0),
                    totalHeal=stats.get('totalHeal', 0),
                    totalUnitsHealed=stats.get('totalUnitsHealed', 0),
                    assists=stats.get('assists', 0),
                    item0=stats.get('item0', 0),
                    item1=stats.get('item1', 0),
                    item2=stats.get('item2', 0),
                    item3=stats.get('item3', 0),
                    item4=stats.get('item4', 0),
                    item5=stats.get('item5', 0),
                    item6=stats.get('item6', 0),
                    visionWardsBoughtInGame=stats.get('visionWardsBought', 0),
                    magicDamageDealtToChampions=stats.get('magicDamageDealtToChampions', 0),
                    physicalDamageDealtToChampions=stats.get('physicalDamageDealtToChampions', 0),
                    totalDamageDealtToChampions=stats.get('totalDamageDealtToChampions', 0),
                    trueDamageDealtToChampions=stats.get('trueDamageDealtPlayer', 0),
                    trueDamageTaken=stats.get('trueDamageTaken', 0),
                    wardsPlaced=stats.get('wardPlaced', 0),
                    neutralMinionsKilledEnemyJungle=stats.get('neutralMinionsKilledEnemyJungle', 0),
                    neutralMinionsKilledTeamJungle=stats.get('neutralMinionsKilledYourJungle', 0),
                    totalTimeCrowdControlDealt=stats.get('totalTimeCrowdControlDealt', 0),
                    playerRole=stats.get('playerRole', 0),
                    playerPosition=stats.get('playerPosition', 0),
                    championId=game['championId'],

                )
                new_stats.participant.add(
                        models.Participant.objects.get(summonerId=summonerId),)
                new_match.stats.add(new_stats)

            except KeyError as e:
                print "Out of API sleeping"
                import time
                time.sleep(30)
        print "Added %d Summoners" % (len(models.Summoners.objects.all()) - curr_summoners)
        print "Added %d Games" % (len(models.Game.objects.all()) - curr_games)



