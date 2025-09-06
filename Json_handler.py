import requests
import json
from pathlib import Path
import math
from Constants import *

def get_player_stats(player_id):
    Updated_id = "".join(["%23",player_id[1:]])
    base_path = Path(__file__).parent
    token_path = base_path / "token.txt"
    file = open(token_path, "r")
    token = file.read().strip('\n')
    query = {"Authorization": f"Bearer {token}"}
    url = "/".join([BASE_URL,PLAYER_URL,Updated_id])
    print(url)
    response = requests.get(url, params=query)
    r: dict = response.json()
    return r


    



def get_local_leaderboard(location_id):
    base_path = Path(__file__).parent
    token_path = base_path / "token.txt"
    file = open(token_path, "r")
    token = file.read().strip('\n')
    query = {"Authorization": f"Bearer {token}"}
    url = "/".join([BASE_URL,LOCATIONS,str(location_id),PATH_OF_LEGENDS_URL,PLAYER_URL])
    print(url)
    response = requests.get(url, params=query)
    print(response)
    r: dict = response.json()
    return r
