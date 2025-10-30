import requests

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

print(specic_match_data["info"]["participants"][9]["win"])
