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

# def champ_win_graph():
#         player_win_stats = models.ParticipantStats.objects.filter(winner=1)
#
#         champ_placed_wins = {}
#
#         for win in player_win_stats:

