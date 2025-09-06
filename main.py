import requests
import json
from pathlib import Path

#This is the json web token generated from your developer.clashroyale.com account
base_path = Path(__file__).parent
token_path = base_path / "token.txt"
file = open(token_path, "r")

token = file.read().strip('\n')

file.close()
base_url = "https://api.clashroyale.com/v1"
# This is an example of enpoint of the reqest, for more check the documentation
endpoint = f"players"

# Correct Authorization header looks like this: "Authorization: Bearer API_TOKEN".
query = {"Authorization": f"Bearer {token}"}
valid = False
while not valid:
    Player_id = input("Enter your ID: ")
    if len(Player_id)  > 9 or len(Player_id) < 9 or Player_id[0] != "#":
        print("Invalid ID")
    else:
        valid = True
Valid_ID = "".join(["%23",Player_id[1:]]).upper()
Final_url = "/".join([base_url,endpoint,Valid_ID,"battlelog"])
print(Final_url)
response = requests.get(Final_url, params=query)

r: dict = response.json()  # Python object

# Save the JSON to a file
with open("clashApi/example_response.json", "w", encoding="utf-8") as response_file:
    json.dump(r, response_file, indent=4)

# Now re-open the file for reading
with open("clashApi/example_response.json", "r", encoding="utf-8") as response_file:
    Battles_json = json.load(response_file)

# for key, value in Battles_json[0].items():
#    print(f"{key} → {value}")
##vlcqgjv0print(Battles_json[0]["opponent"][0])\
cards_dict = {}
index = 0
for battle in range(len(Battles_json)):
    for card_stats in Battles_json[battle]["opponent"][0]["cards"]:
        if cards_dict.get(card_stats["name"]) == None:
            cards_dict[card_stats["name"]] = 1
        else:
            cards_dict[card_stats["name"]] += 1

max_value = max(cards_dict.values())
keys_with_max = [key for key, value in cards_dict.items() if value == max_value]
for key in keys_with_max:
    print(key,cards_dict[key])
print(cards_dict) 

