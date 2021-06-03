from flask import Flask, request


def create_app() -> Flask:
    rbaas = Flask(__name__)
    rbaas.url_map.strict_slashes = False
    
    from rbaas.boss.resources import boss_blueprint
    rbaas.register_blueprint(boss_blueprint)
    # app_config = Config
    # rbaas.config.from_object(app_config)
    return rbaas
