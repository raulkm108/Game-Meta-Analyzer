from src.data.api_client import RiotAPIClient
import pytest

def test_acquire_puuid():

    request = RiotAPIClient(api_key="RGAPI-3e2219b5-edf0-4e48-99f4-971e4fe0e5d2", region="americas")

    user_puuid = request.acquire_puuid(summoner_name="SnowTime", summoner_tag="br1")

    assert isinstance(user_puuid, str)
    assert user_puuid is not None

def test_acquire_match_list():

    request = RiotAPIClient(api_key="RGAPI-3e2219b5-edf0-4e48-99f4-971e4fe0e5d2", region="americas")
    number_of_matches = 10

    user_match_list = request.acquire_match_list(user_puuid="J-QS4qK-tf-R28QaY6m7iYjwjm_wj8FYB7gYxW8Lwiq-Myb3FQb-8QY8ftEUEn1ZXP0d035EcKmNmQ", number_of_matches=number_of_matches)

    assert isinstance(user_match_list, list)
    assert len(user_match_list) == number_of_matches


