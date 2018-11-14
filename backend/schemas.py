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
        "type": "number",
        "required": True,
    },
    "frame": {
        "type": "number",
        "required": True,
    },
}
