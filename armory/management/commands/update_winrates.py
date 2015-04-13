__author__ = 'bob'
import numpy
from armory.models import ParticipantStats, Champions
from django.core.management.base import BaseCommand

def winrate(id):
    games = []
    player_stats = ParticipantStats.objects.all()
    for ps in player_stats:
        try:
            if ps.championId == id:
                games.append(ps.winner)
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
        for ch in champs:
            ch.winrate = winrate(ch.id)
            ch.save()