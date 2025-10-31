import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

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
    
    def get_user_stats(self, user_puuid: str, user_matches_list: list) -> None:
        stats = {
            "wins": 0,
            "loses": 0,
            "Arena": 0,
            "Summoners Rift": 0,
            "Aram":0
        }
        type_mapying ={
            "CHERRY": ["Arena", 0],
            "CLASSIC": ["Summoners Rift", 0],
            "ARAM": ["Aram", 0]
        }

        for match in user_matches_list:
            match_info_ulr = f"https://{self.region}.api.riotgames.com/lol/match/v5/matches/{match}?api_key={self.api_key}"
            match_info = requests.get(match_info_ulr)
            player_index = match_info.json()["metadata"]["participants"].index(user_puuid)
            match_result = match_info.json()["info"]["participants"][player_index]["win"]
            match_type = match_info.json()["info"]["gameMode"]

            for match in type_mapying:
                if match == match_type:
                    stats[type_mapying[match][0]] += 1

            if match_result:
                stats["wins"] += 1
                print(f"{stats["wins"]}th on ({match_type})")

            else:
                stats["loses"] += 1
                print(f"{stats["loses"]}th on ({match_type})")

        return (stats)

    

     
        


        

