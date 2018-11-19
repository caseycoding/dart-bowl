import json
import requests as requests
from tests.fixtures import BASE_URL, player_fixture, game_fixture

shared_test_data = {}
headers = {"Content-Type": "application/json"}


class TestRolls(object):
    def test_roll_player1(self, player_fixture, game_fixture):
        # test spare logic
        test_roll = {"player_id": player_fixture[0][0], "pins_knocked_down": 5}
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == None

        test_roll["pins_knocked_down"] = 5
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == None

        test_roll["pins_knocked_down"] = 5
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == 15

    def test_roll_player2(self, player_fixture, game_fixture):
        # test strike logic and spare totaling
        test_roll = {"player_id": player_fixture[1][0], "pins_knocked_down": 10}
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == None

        test_roll["pins_knocked_down"] = 2
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == None

        test_roll["pins_knocked_down"] = 3
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == 20

        test_roll["pins_knocked_down"] = 9
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == 20

        test_roll["pins_knocked_down"] = 1
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == 20

    def test_roll_player3(self, player_fixture, game_fixture):
        # basic test case
        test_roll = {"player_id": player_fixture[2][0], "pins_knocked_down": 2}
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == None

        test_roll["pins_knocked_down"] = 2
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == 4

        test_roll["pins_knocked_down"] = 9
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 201
        assert roll_res.json()["score"] == 4

        test_roll["pins_knocked_down"] = 2
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 400
        assert roll_res.json()["_error"]["message"] == "Invalid pin value."

    def test_roll_player1_no_score(self, player_fixture, game_fixture):
        test_roll = {"player_id": player_fixture[0][0]}
        roll_res = requests.post(f"{BASE_URL}/games/{game_fixture[0]}/rolls", data=json.dumps(test_roll), headers=headers)
        assert roll_res.status_code == 422
