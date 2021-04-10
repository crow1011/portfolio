from flask import Flask


def init_app():
    '''
    Настройка app перед запуском
    Должна возвращать app
    '''
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    from .passgen import passgen
    with app.app_context():

        app.register_blueprint(passgen.mod_gen)
    return app
