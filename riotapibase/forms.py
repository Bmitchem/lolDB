__author__ = 'bob'
from django import forms


class current_game_form(forms.Form):
    summoner_name = forms.CharField(label="Summoner Name", max_length=35)