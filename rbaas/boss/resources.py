from flask import Blueprint, request
from rbaas.boss.actions import get_boss_health, decrement_boss_health
from time import sleep


boss_blueprint = Blueprint('boss', __name__, url_prefix='')

def get_delay():
    delays = [5, 1]
    while True:
        for delay in delays:
            yield delay
    
    
delay_gen = get_delay()

@boss_blueprint.route('/boss', methods=['GET', 'PUT'])
def boss_controller():
    restful_actions = {
        # 'GET': get_boss_health,
        'GET': lambda x: f'sleeping for {x} {sleep(x)}' ,
        'PUT': decrement_boss_health,
    }
    print()
    return restful_actions[request.method](next(delay_gen))