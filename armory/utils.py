__author__ = 'bob'
import pygal
from riot_api import RiotInterface
from armory import models
import numpy as np
from sets import Set
from armory import constants


def ward_win_graph():
    player_win_stats = models.ParticipantStats.objects.all()
    victory_chances = []
    player_win_stats = player_win_stats.values('winner', 'wardsPlaced')
    for ward in range(0, 100):
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
    games = games.values('gameMode', 'mapId')
    total_games = len(games)
    rift, treeline, aram, dominion = 0, 0, 0, 0
    for g in games:
        if g['gameMode'] == 'CLASSIC':
            if g.get('mapId', 0) in constants.SUMMONERS_RIFT_MAP_CODES:
                rift += 1
            elif g.get('mapId', 0) in constants.TWISTED_TREELINE_MAP_CODES:
                treeline += 1
        elif g['gameMode'] == 'ARAM':
            aram += 1
        elif g['gameMode'] == 'ODIN':
            dominion += 1

    rift_games = float(rift) / float(total_games) * 100
    treeline_games = float(treeline) / float(total_games) * 100
    aram_games = float(aram) / float(total_games) * 100
    dominion_games = float(dominion) / float(total_games) * 100

    from pygal.style import LightStyle

    pie_chart = pygal.Pie(style=LightStyle)
    pie_chart.title = 'Game Mode selection (in %)'
    pie_chart.add('Summoner\'s Rift', rift_games)
    pie_chart.add('Twisted Treeline', treeline_games)
    pie_chart.add('ARAM', aram_games)
    pie_chart.add('Dominion', dominion_games)
    return pie_chart.render()


def champion_damage_distribution(champion):
    player_stats = models.ParticipantStats.objects.all().filter(championId=champion).values(
        'physicalDamageDealtToChampions',
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


def champion_map_pickrate(champion_id):
    relevant_stats = models.ParticipantStats.objects.filter(championId=champion_id).values('summonerId', 'winner')
    relevant_games = models.Game.objects.filter(championId=champion_id).values('mapId', 'summonerId')
    aram_winrate = get_champion_map_pickrate(constants.ARAM_MAD_CODES, relevant_games, relevant_stats)
    classic_winrate = get_champion_map_pickrate(constants.SUMMONERS_RIFT_MAP_CODES, relevant_games, relevant_stats)
    treeline_winrate = get_champion_map_pickrate(constants.TWISTED_TREELINE_MAP_CODES, relevant_games, relevant_stats)
    dominion_winrate = get_champion_map_pickrate(constants.DOMINION_MAP_CODES, relevant_games, relevant_stats)

    from pygal.style import LightStyle

    pie_chart = pygal.Pie(style=LightStyle)
    pie_chart.title = 'Champion popularity per Map (in %)'
    if classic_winrate:
        pie_chart.add('Rift Popularity', classic_winrate / float(len(relevant_games)))
    if treeline_winrate:
        pie_chart.add('Treeline Popularity', treeline_winrate / float(len(relevant_games)))
    if aram_winrate:
        pie_chart.add('Aram Popularity', aram_winrate / float(len(relevant_games)))
    if dominion_winrate:
        pie_chart.add('Dominion Popularity', dominion_winrate / float(len(relevant_games)))
    return pie_chart.render()


def get_champion_map_pickrate(map_codes, relevant_games, relevant_stats):
    pick_rate = 0

    for game in relevant_games:
        if game['mapId'] in map_codes:
            for stat in relevant_stats:
                if stat['summonerId'] == game['summonerId']:
                    pick_rate += 1
    if pick_rate:
        return pick_rate
    else:
        return False


def champion_item_builds(championId):
    relevant_stats = models.ParticipantStats.objects.filter(championId=championId)
    items = models.Items.objects.all().values('id', 'name', 'description')
    built_item_names = []
    for item in items:
        item_names = {
            'id': {
                'name': item['name'],
                'desc': item['description'],
            }
        }
        built_item_names.append(item_names)
    builds = []
    for game in relevant_stats:
        build = Set([
            game.item0,
            game.item1,
            game.item2,
            game.item3,
            game.item4,
            game.item5,
            game.item6,
        ])
        builds.append(build)

    return builds


def champion_popularity(championId, stats):
    games_picked = 0
    for stat in stats:
        if stat.champion == championId:
            games_picked += 1
    if games_picked:
        return (games_picked / float(len(stats))) * 100
    else:
        return 0.00


def get_champion_map_winrate(map_codes, relevant_games, relevant_stats):
    winrate = []

    for game in relevant_games:
        if game['mapId'] in map_codes:
            for stat in relevant_stats:
                if stat['summonerId'] == game['summonerId']:
                    winrate.append(stat['winner'])
    if winrate:
        return np.mean(winrate) * 100
    else:
        return False







