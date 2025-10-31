import requests

class RiotAPIClient:
    def __init__(self, api_key: str, region="americas") -> None:
        self.api_key = api_key
        self.region = region

    def acquire_puuid(self, summoner_name:str, summoner_tag:str) -> str:
        user_info_url = f"https://{self.region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{summoner_tag}?api_key={self.api_key}"
        user_info = requests.get(user_info_url)
        user_puuid = user_info.json()["puuid"]
        return user_puuid
    
    def acquire_match_list(self, user_puuid: str, number_of_matches: int) -> list:
        user_match_history_url = f"https://{self.region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{user_puuid}/ids?start=0&count={number_of_matches}&api_key={self.api_key}"
        user_matches_history = requests.get(user_match_history_url)
        user_matches_list = user_matches_history.json()
        return user_matches_list