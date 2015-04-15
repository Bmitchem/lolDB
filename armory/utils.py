__author__ = 'bob'
import pygal
from riot_api import RiotInterface
from armory import models
import numpy as np

def ward_win_graph():
    player_win_stats = models.ParticipantStats.objects.all()
    victory_chances = []
    player_win_stats = player_win_stats.values('winner', 'wardsPlaced')
    for ward in range(0,100):
        victory_chances.append(game_ward_win(ward, player_win_stats))

    from pygal.style import LightStyle
    line_chart = pygal.Line(style=LightStyle)
    line_chart.title = 'Ward Victories '
    line_chart.x_labels = map(str, range(0, 26))
    line_chart.add('Wards Placed', victory_chances[1:26:])
    return line_chart.render()

def game_ward_win(ward_num, player_stats):
    game_results = []
    for game in player_stats:
        if game['wardsPlaced'] == ward_num:
            game_results.append(game['winner'])

    victory_chance = np.mean(game_results) * 100
    return victory_chance


def game_type_graph():
    games = models.Game.objects.all()
    games = games.values('gameMode')
    total_games = len(games)
    classic, aram, dominion = 0, 0, 0
    for g in games:
        if g['gameMode'] == 'CLASSIC':
            classic += 1
        elif g['gameMode'] == 'ARAM':
            aram += 1
        elif g['gameMode'] == 'ODIN':
            dominion += 1
    classic_games = float(classic) / float(total_games) * 100
    aram_games = float(aram) / float(total_games) * 100
    dominion_games = float(dominion) / float(total_games) * 100



    from pygal.style import LightStyle
    pie_chart = pygal.Pie(style=LightStyle)
    pie_chart.title = 'Game Mode selection (in %)'
    pie_chart.add('Summoner\'s Rift', classic_games)
    pie_chart.add('ARAM', aram_games)
    pie_chart.add('Dominion', dominion_games)
    return pie_chart.render()

def champion_damage_distribution(champion):
    player_stats = models.ParticipantStats.objects.all().filter(championId=champion).values('physicalDamageDealtToChampions',
                                                                                 'magicDamageDealtToChampions',
                                                                                 'trueDamageDealtToChampions',
                                                                                 'totalDamageDealtToChampions')
    total_damage = champion_total_damage(player_stats)
    phys_damage = champion_damage_physical(player_stats)
    magic_damage = champion_damage_magic(player_stats)
    true_damage = champion_damage_true(player_stats)





    from pygal.style import LightStyle
    pie_chart = pygal.Pie(style=LightStyle)
    pie_chart.title = 'Damage Distribution (in %)'
    if phys_damage:
        pie_chart.add('Physical Damage', phys_damage / float(total_damage))
    if magic_damage:
        pie_chart.add('Magic Damage', magic_damage / float(total_damage))
    if true_damage:
        pie_chart.add('True Damage', true_damage / float(total_damage))
    return pie_chart.render()

def champion_damage_physical(relevant_player_stats):
    physical_damage_per_game = []
    for game in relevant_player_stats:
        physical_damage_per_game.append(game['physicalDamageDealtToChampions'])
        
    return np.mean(physical_damage_per_game)


def champion_damage_true(relevant_player_stats):
    true_damage_per_game = []
    for game in relevant_player_stats:
        true_damage_per_game.append(game['trueDamageDealtToChampions'])
        
    return np.mean(true_damage_per_game)

def champion_damage_magic(relevant_player_stats):
    magic_damage_per_game = []
    for game in relevant_player_stats:
        magic_damage_per_game.append(game['magicDamageDealtToChampions'])
        
    return np.mean(magic_damage_per_game)

def champion_total_damage(relevant_player_stats):
    total_damage_per_game = []
    for game in relevant_player_stats:
        total_damage_per_game.append(game['totalDamageDealtToChampions'])
        
    return np.mean(total_damage_per_game)

