__author__ = 'bob'
from django.core.management.base import BaseCommand, CommandError
from riot_api import RiotInterface
from armory import models
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        ri = RiotInterface()
        ri.update_champions()
        ri.update_items()
