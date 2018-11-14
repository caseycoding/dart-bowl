# Schema definition, based on Cerberus grammar. Check the Cerberus project
# (https://github.com/pyeve/cerberus) for details.
game_schema = {}


player_schema = {
    'displayName': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
        'required': True,
    },
}
