from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from riot_api import RiotInterface

def index(request):
    #list of current games
    client = RiotInterface()
    

    return render_to_response('index.html', {})
