import schemas

DOMAIN = {
    "players": {"schema": schemas.player_schema},
    "games": {"schema": schemas.create_game_schema},
    "roll": {"schema": schemas.roll_schema, "url": "games/<regex('[a-f0-9]{24}'):game_id>/rolls"},
}

# database
MONGO_DBNAME = "dart-bowl"
MONGO_HOST = "db"
MONGO_PORT = 27017

RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]

X_DOMAINS = ["localhost", "www.dartbowl.com"]
BANDWIDTH_SAVER = False  # allows for the full object to be returned on creation
