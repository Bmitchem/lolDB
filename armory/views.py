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
from django.template.defaultfilters import slugify
from django.http import HttpResponse
import datetime

# @cache_page(60 * 15)
def champion(request):
    champ_id = 1
    if request.method == 'GET':
        champ_id = request.GET['champ_id']

    picked_champion = None
    champs = models.Champions.objects.filter(freeToPlay=1).order_by('-winrate')
    champ_list = models.Champions.objects.all().values()
    damage_graph = utils.champion_damage_distribution(champ_id)
    game_mode_winrate = utils.champion_map_pickrate(champ_id)
    for champ in champ_list:
        if champ['id'] == int(champ_id):
            picked_champion = champ
            break

    return HttpResponse(render_to_response('armory/champion.html', {
        'champ': picked_champion['name'],
        'champion_damage': damage_graph,
        'game_mode_winrate': game_mode_winrate,
        'champ_list': champ_list,
        'champions': champs,
        'page_title': picked_champion['name'],
        'body_title': '%s\'s Vital Stats' % picked_champion['name'],
        'page_title_image': picked_champion['image']

    }))


def champion_search(request):
    champ_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']

    champ_list = get_champion_list_suggest(8, starts_with=starts_with)

    template = Template("""

                        {% for champ in  champ_list %}
                        <li>
                            <a href="/armory/champion/{{ champ.id }}">{{ champ.name }}
                            <img src="http://ddragon.leagueoflegends.com/cdn/5.7.1/img/champion/{{ champ.image }}" style="height: 2em;"/></a>
                        </li>
                        {% endfor %}
                        </div>
        """)
    context = Context({'champ_list': champ_list, 'search_completed': bool(champ_list), })

    return HttpResponse(template.render(context))


def player_search(request):
    context = RequestContext(request)
    champ_list = []
    if request.method == 'GET':
        player_name = request.GET['suggestion']
    else:
        return

    ri = RiotInterface()

    player_id_resp = ri.pull_summoner_id(player_name)
    if player_id_resp:
        player_id_resp = player_id_resp.get(player_name.lower(), None)
        if player_id_resp:
            player_id_resp = player_id_resp.get('id', None)
    else:
        return
    player_match_history = ri.match_history(player_id_resp).json()
    champs = []
    for match in player_match_history['matches']:
        match['matchCreation'] = datetime.datetime.fromtimestamp(match['matchCreation'] / 1000.0)
        champs.append(match['participants'][0]['championId'])

    champ_list = models.Champions.objects.filter(id__in=champs)

    return HttpResponse(render_to_response('armory/player_match_history.html',
                                           {'match_json': player_match_history, 'player_name': player_name,
                                            'champ_list': champ_list}))


def match_info_update(request):
    if request.method == 'GET':
        match = request.GET['match']
    else:
        return

    ri = RiotInterface()
    match_detail = ri.pull_match_info(match)

    team_blue = []
    team_red = []

    for participant in match_detail['participants']:
        print "participant info-- Lane: %s Role: %s" % (participant['timeline']['lane'], participant['timeline']['role'])
        participant['championId'] = models.Champions.objects.filter(id=participant['championId']).first()
        if participant['teamId'] == 100:
            team_red.append(participant)
        else:
            team_blue.append(participant)
    return HttpResponse(render_to_response('armory/match_timeline_chart.html',{
        'team_blue':team_blue,
        'team_red':team_red,
    }))



def get_champion_list_suggest(max_results=0, starts_with=''):
    champ_list = []
    if starts_with:
        champ_list = models.Champions.objects.filter(name__istartswith=starts_with)
    else:
        champ_list = []

    if max_results > 0:
        if len(champ_list) > max_results:
            champ_list = champ_list[:max_results]

    return champ_list
