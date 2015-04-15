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
from django.template import Context, Template


# @cache_page(60 * 15)
def champion(request, champion_name):
    champs = models.Champions.objects.filter(freeToPlay=1).order_by('-winrate')
    champ_list = models.Champions.objects.all().values()
    picked_champion = models.Champions.objects.get(name=champion_name)
    graph = utils.champion_damage_distribution(picked_champion.id)
    for champ in champ_list:
        if champ['name'] == picked_champion:
            picked_champion = champ
            break




    return render_to_response('armory/champion.html', {
        'champ': picked_champion.name,
        'champion_damage': graph,
        'champ_list': champ_list,
        'champions': champs,
        'page_title': champion_name,
        'body_title': '%s\'s Vital Stats' % champion_name,

    })
