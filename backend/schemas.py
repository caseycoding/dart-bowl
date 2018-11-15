# Schema definition, based on Cerberus grammar. Check the Cerberus project
# (https://github.com/pyeve/cerberus) for details.
game_schema = {
    "lane": {
        "type": "number",
        "required": True,
    },
    "players": {
        "type": "list",
        "required": True,
        "schema": {
            "type": "objectid",
        }
    },
    "scores": {
        "type": "dict",
        "required": False,
        "keyschema": {
            "type": "objectid",
        },
        "valueschema": {
            "type": "dict",
            "schema": {
                "total_score": {
                    "type": "number",
                },
                "player_id": {
                    "type": "objectid",
                },
                "dispay_name": {
                    "type": "string",
                }, 
                "frames": {
                    "type": "list",
                }
            }
        }
    }
}

player_schema = {
    "displayName": {
        "type": "string",
        "minlength": 1,
        "maxlength": 10,
        "required": True,
    },
}

roll_schema = {
    "game": {
        "type": "objectid",
        "required": True,
        "data_relation": {
            "resource": "games",
            "field": "_id",
                     "embeddable": True
        },
    },
    "player": {
        "type": "objectid",
        "required": True,
        "data_relation": {
            "resource": "players",
            "field": "_id",
                     "embeddable": True
        },
    },
    "pins": {
        "type": "string", # string to handle strikes
        "required": True,
    }
}
