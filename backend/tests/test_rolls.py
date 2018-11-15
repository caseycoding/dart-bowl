import json
import requests as requests
from tests.fixtures import BASE_URL, player_fixture, game_fixture

shared_test_data = {}
headers = {"Content-Type": "application/json"}


class TestRolls(object):
    def test_roll_player1(self, player_fixture, game_fixture):
        new_roll = {
          "game": game_fixture[0], 
          "player": player_fixture[0][0],
          "pins": "5",
        }
        roll_res = requests.post(f"{BASE_URL}/rolls",
                          data=json.dumps(new_roll), headers=headers)
        assert roll_res.status_code == 201
        data = roll_res.json()

        assert data["frame"] == 0
        assert data["total_score"] == 5

    def test_roll_player2(self, player_fixture, game_fixture):
        # tests that a single strike doesn't return a score because the next two rolls haven't been completed
        new_roll = {
            "game": game_fixture[0],
            "player": player_fixture[1][0],
            "pins": "X",
        }
        roll_res = requests.post(f"{BASE_URL}/rolls",
                                 data=json.dumps(new_roll), headers=headers)
        assert roll_res.status_code == 201
        data = roll_res.json()

        assert data["frame"] == 0
        assert data["total_score"] == None
