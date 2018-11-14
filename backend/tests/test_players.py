import requests
BASE_URL = "http://localhost:5000"

shared_test_data = {}

class TestPlayers(object):

  def test_create_player(self):
    new_player = {
      "displayName": "Casey"
    }
    r = requests.post(f"{BASE_URL}/players", data=new_player)
    assert r.status_code == 201

    # save player id for later
    data = r.json()
    shared_test_data["_id"] = data["_id"]
    shared_test_data["_etag"] = data["_etag"]

  def test_patch_player(self):
    new_player = {
        "displayName": "CaseyB"
    }
    print(f"{BASE_URL}/players/{shared_test_data['_id']}")
    r = requests.patch(f"{BASE_URL}/players/{shared_test_data['_id']}", 
                      data=new_player,
                      headers={"If-Match": shared_test_data["_etag"]}
                      )
    print(r.text)
    assert r.status_code == 200

    data = r.json()
    shared_test_data["_etag"] = data["_etag"]

  def test_delete_player(self):
    r = requests.delete(f"{BASE_URL}/players/{shared_test_data['_id']}",
                      headers={"If-Match": shared_test_data["_etag"]}
                      )
    assert r.status_code == 204

