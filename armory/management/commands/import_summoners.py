__author__ = 'bob'
from django.core.management.base import BaseCommand, CommandError
from riot_api import RiotInterface
from armory import models
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        summoner_list = models.Summoners.objects.all().order_by('-dateAdded')

        ri = RiotInterface()
        for index, summoner in enumerate(summoner_list):
            if index % 500 == 0 and index != 0:
                time.sleep(60)
            if index % 10 == 0 and index != 0:
                time.sleep(10)
            else:
                print "Importing history for " + str(summoner.summonerId)
                ri.import_summoner_id_from_pull(summoner.summonerId)
