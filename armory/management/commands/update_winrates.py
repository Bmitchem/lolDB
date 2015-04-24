__author__ = 'bob'
import numpy
from armory.models import ParticipantStats, Champions, Game, Participant
from django.core.management.base import BaseCommand
from armory import utils, constants

def winrate(id, player_stats):
    games = []
    for ps in player_stats:
        try:
            if ps['championId'] == id:
                games.append(ps['winner'])
        except IndexError as e:
            print "print errored out", ps.id
            continue
    if games:
        return_value = numpy.mean(games) * 100
        return "%.2f" % return_value
    else:
        return 0.0



class Command(BaseCommand):
    def handle(self, *args, **options):
        champs = Champions.objects.all()
        player_stats = ParticipantStats.objects.all().values('championId', 'winner')
        players = Participant.objects.all()
        games = Game.objects.all()
        for ch in champs:
            ch.winrate = winrate(ch.id, player_stats)
            ch.popularity = utils.champion_popularity(ch.id, players)
            ch.aram_winrate = utils.get_champion_map_winrate(constants.ARAM_MAD_CODES,
                                                             games.filter(championId=ch.id).values('mapId', 'summonerId'),
                                                             player_stats.filter(championId=ch.id).values('winner', 'summonerId'))
            ch.dominion_winrate = utils.get_champion_map_winrate(constants.DOMINION_MAP_CODES,
                                                             games.filter(championId=ch.id).values('mapId', 'summonerId'),
                                                             player_stats.filter(championId=ch.id).values('winner', 'summonerId'))
            ch.rift_winrate = utils.get_champion_map_winrate(constants.SUMMONERS_RIFT_MAP_CODES,
                                                             games.filter(championId=ch.id).values('mapId', 'summonerId'),
                                                             player_stats.filter(championId=ch.id).values('winner', 'summonerId'))
            ch.treeline_winrate = utils.get_champion_map_winrate(constants.TWISTED_TREELINE_MAP_CODES,
                                                             games.filter(championId=ch.id).values('mapId', 'summonerId'),
                                                             player_stats.filter(championId=ch.id).values('winner', 'summonerId'))
            ch.save()