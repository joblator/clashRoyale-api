from request_fethcher import get_player_stats 
def top_players_cards(top_players_dict):
    cards_dict = {}
    num_players = 0
    player_amount = len(top_players_dict["items"])
    done = 0
    for player in range(player_amount):
        players_stats_dict = (get_player_stats(top_players_dict["items"][player]["tag"]))
        print(f"there are {player_amount-done } players left to check")
        for card_stats in players_stats_dict["currentDeck"]:
            cards_dict[card_stats["name"]] = cards_dict.get(card_stats["name"],0) + 1
            # if cards_dict.get(card_stats["name"]) == None:
            #     cards_dict[card_stats["name"]] = 1
            # else:
            #     cards_dict[card_stats["name"]] += 1
        num_players += 1
        done += 1
    cards_dict = dict(sorted(cards_dict.items(), key=lambda item: item[1], reverse=True))
    return num_players,cards_dict
def battleLog_cards(player_dict):
    matches = 0
    cards_dict = {}
    for battle in range(len(player_dict)):
        for card_stats in player_dict[battle]["opponent"][0]["cards"]:
            if cards_dict.get(card_stats["name"]) == None:
                cards_dict[card_stats["name"]] = 1
            else:
                cards_dict[card_stats["name"]] += 1
        matches += 1
    cards_dict = dict(sorted(cards_dict.items(), key=lambda item: item[1], reverse=True))
    return matches,cards_dict
