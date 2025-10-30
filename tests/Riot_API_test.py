import requests
import datetime as dt

ti = dt.datetime.now()

api_key = 'RGAPI-3e2219b5-edf0-4e48-99f4-971e4fe0e5d2'

my_puuid = 'J-QS4qK-tf-R28QaY6m7iYjwjm_wj8FYB7gYxW8Lwiq-Myb3FQb-8QY8ftEUEn1ZXP0d035EcKmNmQ'

api_url_user = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/SnowTime/br1?api_key={api_key}'

data = requests.get(api_url_user)

player_info = data.json()

api_url_matches = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{my_puuid}/ids?start=0&count=20&api_key={api_key}'

data_matches = requests.get(api_url_matches)

player_info_match = data_matches.json()

match_id = player_info_match[0]

api_url_specifc_match = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}'

data_specfic_match = requests.get(api_url_specifc_match)

specic_match_data = data_specfic_match.json()

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

for match in user_matches_list:
    match_info_ulr = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}"
    match_info = requests.get(match_info_ulr)
    player_index = match_info.json()["metadata"]["participants"].index(user_puuid)
    match_result = match_info.json()["info"]["participants"][player_index]["win"]
    if match_result:
        wins += 1
        print(f"One Win ({wins})")

    else:
        loses += 1
        print(f"One Lose ({loses})")

print(f"The summoner {summoner_name} has a winrate of {round(wins/(wins + loses), 2)} in the last {number_of_matches} games")

tf = dt.datetime.now()

print (tf - ti)
