from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from riot_api import RiotInterface
from armory import models
import pygal
from armory import utils
from django.views.decorators.cache import cache_page

@cache_page(60*15)
def index(request):
    #list of current games

    champs = models.Champions.objects.filter(freeToPlay=1)
    champ_list = models.Champions.objects.all()
    champ_list.all()
    # graph = utils.ward_win_graph()
    graph = utils.game_type_graph()


    return render_to_response('index.html', {'champions' : champs, 'graph': graph, 'champ_list': champ_list})

