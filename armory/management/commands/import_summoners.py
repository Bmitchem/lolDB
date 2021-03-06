__author__ = 'bob'
from django.core.management.base import BaseCommand, CommandError
from riot_api import RiotInterface
from armory import models
import sys
from time import sleep
import random


class Command(BaseCommand):
    def handle(self, *args, **options):

        summoner_list = models.Summoners.objects.all().order_by('-dateAdded')
        query_set = []
        for i in range(3000):
            query_set.append(summoner_list[random.randint(0, len(summoner_list))])

        ri = RiotInterface()
        del summoner_list

        for index, summoner in enumerate(query_set):
            print "Importing history for " + str(summoner.summonerId)
            ri.import_summoner_id_from_pull(summoner.summonerId)
            summoners_left = len(query_set) - index
            print "Completed %d, we have %d summoners left in this run" % (index, summoners_left)
            # ri.import_summoner_id_from_pull(25500646)