from flask_restplus import Api
from flask import Flask


def init_app():
    '''
    Настройка app перед запуском
    Должна возвращать app
    '''
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    from api_v1 import blueprint as api1

    with app.app_context():
        app.register_blueprint(api1)
    return app


app = init_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
