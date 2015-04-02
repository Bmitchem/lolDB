__author__ = 'bob'
import requests
from django.conf import settings
from armory import models
import logging


class RiotInterface(object):

    def __init__(self):
        pass
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
            print "saving item: ", items.get('data')[key]['name']
            i, new = models.Items.objects.get_or_create(id=items.get('data')[key]['id'],
                                                        defaults={
                                                            'name':items.get('data')[key]['name'],
                                                            'group':items.get('data')[key].get('group',None),
                                                            'description':items.get('data')[key]['description'],
                                                            'plaintext':items.get('data')[key].get('plaintext', None)
                                                        })