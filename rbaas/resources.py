from flask import current_app

@current_app.route('/boss', methods=['GET', 'PUT'])
def boss_controller():
    restful_actions = {
        'GET': get_boss_health,
        'PUT': decrement_boss_health,
    }

    return restful_actions.get(request.method, lambda _: f'{request.method} method not supported')()