__author__ = 'bob'
from django.core.management.base import BaseCommand, CommandError
from riot_api import RiotInterface
from armory import models
import time

def compute():
    empty_stats = models.ParticipantStats.objects.filter(summonerId=0)
    for stat in empty_stats:
        print "Checking %s out of %d" % (stat.id, len(empty_stats))
        stat_summoner = stat.participant.first()
        stat.summonerId = stat_summoner.summonerId
        stat.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        compute()
