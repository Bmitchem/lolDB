__author__ = 'bob'
import pygal
from riot_api import RiotInterface
from armory import models

def ward_win_graph():
    player_win_stats = models.ParticipantStats.objects.filter(winner=1)

    ward_placed_wins = [0 for x in range(100)]
    ward_killed_wins = [0 for x in range(100)]

    for win in player_win_stats:
        ward_placed_wins[win.wardsPlaced] += 1

    from pprint import pprint
    pprint(ward_killed_wins)

    for win in range(len(ward_placed_wins)):

        ward_placed_wins[win] = (float(ward_placed_wins[win]) / float(len(player_win_stats))) * 100

    from pprint import pprint
    # pprint(ward_killed_wins)

    from pygal.style import LightStyle
    line_chart = pygal.Line(style=LightStyle)
    line_chart.title = 'Ward Victories '
    line_chart.x_labels = map(str, range(0, 26))
    line_chart.add('Wards Placed', ward_placed_wins[1:26:])
    return line_chart.render()

def game_type_graph():
    games = models.Game.objects.all()
    total_games = len(games)
    classic_games = float(len(models.Game.objects.filter(gameMode='CLASSIC'))) / float(total_games) * 100
    aram_games = float(len(models.Game.objects.filter(gameMode='ARAM'))) / float(total_games) * 100
    dominion_games = float(len(models.Game.objects.filter(gameMode='ODIN'))) / float(total_games) * 100



    from pygal.style import LightStyle
    pie_chart = pygal.Pie(style=LightStyle)
    pie_chart.title = 'Game Mode selection (in %)'
    pie_chart.add('Summoner\'s Rift', classic_games)
    pie_chart.add('ARAM', aram_games)
    pie_chart.add('Dominion', dominion_games)
    return pie_chart.render()

