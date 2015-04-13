__author__ = 'bob'
import numpy
from armory.models import ParticipantStats
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        player_stats = ParticipantStats.objects.filter(championId=0)
        for ps in player_stats:
            try:
                player_set = ps.participant.all()
                for player in player_set:
                    ps.championId = player.champion
                    ps.save()
            except IndexError as e:
                print "print errored out", ps.id
                continue
        ParticipantStats.objects.filter(championId=0).delete()