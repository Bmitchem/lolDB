from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from riot_api import RiotInterface
from armory import models
import pygal
from armory import utils

def index(request):
    #list of current games

    champs = models.Champions.objects.filter(freeToPlay=1)
    # ward_graph = utils.ward_win_graph()
    map_graph = utils.game_type_graph()


    return render_to_response('index.html', {'champions' : champs, 'graph': map_graph})

