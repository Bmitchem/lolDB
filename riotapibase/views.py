from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from riot_api import RiotInterface
from armory import models
import pygal
from armory import utils
from django.views.decorators.cache import cache_page
import json
import cPickle
from os import path


@cache_page(60 * 15)
def index(request):
    # list of current games
    main_page_stats = []
    champs = models.Champions.objects.filter(freeToPlay=1).order_by('-winrate')
    champ_list = models.Champions.objects.all().order_by('name')
    players = models.ParticipantStats.objects.count()
    main_page_stats.append({
        'name': 'Games recorded',
        'info': players
    })
    summoners = models.Summoners.objects.count()
    main_page_stats.append({
        'name': 'Summoners Stored',
        'info': summoners
    })

    if path.isfile('front_page_graph.json'):
        graph = cPickle.load(open('front_page_graph.json', 'r'))
    else:
        graph = utils.game_type_graph()
        cPickle.dump(graph, open('front_page_graph.json', 'w+'))

    return render_to_response('index.html', {
        'main_page_stats': main_page_stats,
        'champions': champs,
        'graph': graph,
        'champ_list': champ_list,
        'page_title': 'Dashboard',
        'body_title': 'Chart of the Day!',
    })

