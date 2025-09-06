import requests
import json
from pathlib import Path
import math
from Json_handler import *
from Constants import *
top_players_dict = get_local_leaderboard(USA_LOCATION_ID)

cards_dict = {}
players = 0
for player in range(len(top_players_dict["items"])):
    players_stats_dict = (get_player_stats(top_players_dict["items"][player]["tag"]))
    for card_stats in players_stats_dict["currentDeck"]:
        if cards_dict.get(card_stats["name"]) == None:
            cards_dict[card_stats["name"]] = 1
        else:
            cards_dict[card_stats["name"]] += 1
    players += 1

cards_dict = dict(sorted(cards_dict.items(), key=lambda item: item[1], reverse=True))
for key in cards_dict:
    percent = math.floor(cards_dict[key] / players * 100)
    print(F"{percent}% of players of the top players use {key}")

