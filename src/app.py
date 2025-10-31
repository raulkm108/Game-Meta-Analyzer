from data.api_client import RiotAPIClient
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

request = RiotAPIClient(api_key=API_KEY,region="americas")

user_puuid = request.acquire_puuid(summoner_name="SnowTime", summoner_tag="br1")

print(user_puuid)

number_of_matches = 10
user_match_list = request.acquire_match_list(user_puuid=user_puuid, number_of_matches=number_of_matches)

print(user_match_list)

user_stats = request.get_user_stats(user_puuid=user_puuid, user_matches_list=user_match_list)

print(user_stats)