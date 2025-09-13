import requests
import json
from pathlib import Path
import math
from request_fethcher import *
from Constants import *
import json_handler
import time
top_players_dict = get_local_leaderboard(USA_LOCATION_ID)
start = time.time()
players , cards_dict = json_handler.top_players_cards(top_players_dict) 
for key in cards_dict:
    percent = math.floor(cards_dict[key] / players * 100)
    print(F"{percent}% of players of the top players use {key}")
print(f"it took {time.time() - start} seconds ")

