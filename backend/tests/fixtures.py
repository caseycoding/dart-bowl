import json
import requests
import pytest

BASE_URL = "http://localhost:5000"


@pytest.fixture(scope="module")
def player_fixture():
    player_names = ["Theodore", "Jeff", "Walter"]
    players = []
    for player in player_names:
        player_res = requests.post(f"{BASE_URL}/players", data={"displayName": player})
        player_data = (player_res.json()["_id"], player_res.json()["_etag"])
        players.append(player_data)

    yield players

    # cleanup
    for player in players:
        player_del = requests.delete(f"{BASE_URL}/players/{player[0]}", headers={"If-Match": player[1]})
        assert player_del.status_code == 204


@pytest.fixture(scope="module")
def game_fixture(player_fixture):
    players = [_id for _id, _etag in player_fixture]
    new_game = {"lane": 15, "players": players}
    game_res = requests.post(f"{BASE_URL}/games", data=json.dumps(new_game), headers={"Content-Type": "application/json"})

    game_data = (game_res.json()["_id"], game_res.json()["_etag"])
    yield game_data

    # cleanup
    game_del = requests.delete(f"{BASE_URL}/games/{game_data[0]}", headers={"If-Match": game_data[1]})
    assert game_del.status_code == 204
