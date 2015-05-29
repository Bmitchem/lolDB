__author__ = 'bob'

from django.http import HttpResponse
from django.conf import settings
from riot_api import RiotInterface

def MatchRequest(request):
    print request
    if request.method == 'GET':
        player_id = request.GET['player_id']
    else:
        return None

    ri = RiotInterface()
    match_history = ri.match_history(player_id)
    return match_history
