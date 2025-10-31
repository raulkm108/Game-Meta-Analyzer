import requests
import datetime as dt

ti = dt.datetime.now()

api_key = 'RGAPI-3e2219b5-edf0-4e48-99f4-971e4fe0e5d2'

summoner_name = input("Type your summoner name: ")
game_tag = input("Type your ingame tag: ")
number_of_matches = input("How many matches you wanna analyze: ")

user_info_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{game_tag}?api_key={api_key}"

user_info = requests.get(user_info_url)

user_puuid = user_info.json()["puuid"]

user_matches_list_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{user_puuid}/ids?start=0&count={number_of_matches}&api_key={api_key}"

user_matches_info = requests.get(user_matches_list_url)

user_matches_list = user_matches_info.json()

wins = 0
loses= 0
arams = 0
summoners_rifts = 0
arenas = 0

for match in user_matches_list:
    match_info_ulr = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}"
    match_info = requests.get(match_info_ulr)
    player_index = match_info.json()["metadata"]["participants"].index(user_puuid)
    match_result = match_info.json()["info"]["participants"][player_index]["win"]
    match_type = match_info.json()["info"]["gameMode"]

    
    if match_type == "CHERRY":
        match_type = "ARENA"
        arenas += 1

    if match_type == "CLASSIC":
        match_type = "SUMMONER'S RIFT"
        summoners_rifts += 1

    if match_type == "ARAM":
        arams += 1

    if match_result:
        wins += 1
        print(f"One Win ({wins} out of {wins + loses}) ({match_type})")

    else:
        loses += 1
        print(f"One Lose ({loses} out of {wins + loses}) ({match_type})")

print(f"""The summoner {summoner_name} has a winrate of {round(wins/(wins + loses), 2)} in the last {number_of_matches} games
      {summoners_rifts} being Summoners Rift's
      {arams} being Arams
      {arenas} being Arenas""")

tf = dt.datetime.now()

print (tf - ti)
