import os
import schemas

DOMAIN = {
    "players": {
        "schema": schemas.player_schema
    },
    "games": {
        "schema": schemas.game_schema
    },
    "rolls": {
        "schema": schemas.roll_schema
    }
}

# database
MONGO_DBNAME = "dart-bowl"
MONGO_HOST = "db"
MONGO_PORT = 27017

RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]

X_DOMAINS = ["localhost", "www.dartbowl.com"]

