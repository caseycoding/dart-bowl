# Schema definition, based on Cerberus grammar. Check the Cerberus project
# (https://github.com/pyeve/cerberus) for details.
create_game_schema = {
    "lane": {"type": "number", "required": False},
    "players": {"type": "list", "required": True, "schema": {"type": "objectid"}},
}

roll_schema = {
    "player_id": {"type": "objectid", "required": True},
    "pins_knocked_down": {"type": "number", "required": True},
}

player_schema = {
    "displayName": {"type": "string", "minlength": 1, "maxlength": 10, "required": True}
}
