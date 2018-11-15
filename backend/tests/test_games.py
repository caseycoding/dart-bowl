import json
import requests as requests
from tests.fixtures import BASE_URL, player_fixture

shared_test_data = {}
headers = {"Content-Type": "application/json"}


class TestGames(object):
    def test_create_game(self, player_fixture):
        players = [_id for _id, _etag in player_fixture]
        new_game = {"lane": 12, "players": players}
        r = requests.post(f"{BASE_URL}/games", data=json.dumps(new_game), headers=headers)
        assert r.status_code == 201

        # save game id for later
        data = r.json()
        shared_test_data["_id"] = data["_id"]
        shared_test_data["_etag"] = data["_etag"]

    def test_patch_game(self):
        change_lane = {"lane": 8}
        r = requests.patch(f"{BASE_URL}/games/{shared_test_data['_id']}", data=change_lane, headers={"If-Match": shared_test_data["_etag"]})
        assert r.status_code == 200

        data = r.json()
        shared_test_data["_etag"] = data["_etag"]

    def test_delete_game(self):
        r = requests.delete(f"{BASE_URL}/games/{shared_test_data['_id']}", headers={"If-Match": shared_test_data["_etag"]})
        assert r.status_code == 204
