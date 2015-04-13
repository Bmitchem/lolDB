__author__ = 'bob'
from django.core.management.base import BaseCommand, CommandError
from riot_api import RiotInterface
from armory import models
import sys
from time import sleep

class Command(BaseCommand):
    def handle(self, *args, **options):
        summoner_list = models.Summoners.objects.all().order_by('-dateAdded')

        ri = RiotInterface()
        counter = 0
        for index, summoner in enumerate(summoner_list):
            counter += 1
            if counter < 30:
                print "Importing history for " + str(summoner.summonerId)
                ri.import_summoner_id_from_pull(summoner.summonerId)
            else:
                sys.exit()
        # ri.import_summoner_id_from_pull(25500646)