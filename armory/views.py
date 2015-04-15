__author__ = 'bob'
from django.shortcuts import render

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from riot_api import RiotInterface
from armory import models
import pygal
from armory import utils
import models
from django.views.decorators.cache import cache_page

@cache_page(60*15)
def champion(request, champion_name):
        champ_data = models.Champions.objects.get(name=champion_name)

        return render_to_response('index.html', {'champion_data' : champ_data})
