from src.data.api_client import RiotAPIClient
import pytest
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def test_acquire_puuid():

    request = RiotAPIClient(api_key=API_KEY, region="americas")

    user_puuid = request.acquire_puuid(summoner_name="SnowTime", summoner_tag="br1")

    assert isinstance(user_puuid, str)
    assert user_puuid is not None

def test_acquire_match_list():

    request = RiotAPIClient(api_key=API_KEY, region="americas")
    number_of_matches = 10

    user_match_list = request.acquire_match_list(user_puuid="J-QS4qK-tf-R28QaY6m7iYjwjm_wj8FYB7gYxW8Lwiq-Myb3FQb-8QY8ftEUEn1ZXP0d035EcKmNmQ", number_of_matches=number_of_matches)

    assert isinstance(user_match_list, list)
    assert len(user_match_list) == number_of_matches

def test_get_user_stats():

    request = RiotAPIClient(api_key=API_KEY, region="americas")

    number_of_matches = 10
    user_match_list = request.acquire_match_list(user_puuid="J-QS4qK-tf-R28QaY6m7iYjwjm_wj8FYB7gYxW8Lwiq-Myb3FQb-8QY8ftEUEn1ZXP0d035EcKmNmQ", number_of_matches=number_of_matches)
    stats_of_user = request.get_user_stats(user_puuid="J-QS4qK-tf-R28QaY6m7iYjwjm_wj8FYB7gYxW8Lwiq-Myb3FQb-8QY8ftEUEn1ZXP0d035EcKmNmQ", user_matches_list=user_match_list)

    assert "wins" in stats_of_user
    assert "loses" in stats_of_user
    assert "Aram" in stats_of_user
    assert "Summoners Rift" in stats_of_user
    assert "Arena" in stats_of_user

    assert stats_of_user["wins"] is not None
    assert stats_of_user["loses"] is not None
    assert stats_of_user["Aram"] is not None
    assert stats_of_user["Summoners Rift"] is not None
    assert stats_of_user["Arena"] is not None



