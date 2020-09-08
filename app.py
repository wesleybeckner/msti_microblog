from flask import Flask
from example_blueprint import *
from importlib import import_module

app = Flask(__name__)
app.register_blueprint(example_blueprint)

def register_blueprints(app):
    for module_name in ('DashExample'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(selenium=False):
    app = Flask(__name__, static_folder='base/static')
    # app.config.from_object(config)
    if selenium:
        app.config['LOGIN_DISABLED'] = True
    # register_extensions(app)
    app.register_blueprint(example_blueprint)
    # register_blueprints(app)
    # configure_database(app)
    # configure_logs(app)
    # apply_themes(app)
    app = Add_Dash(app)
    # app = Dash_App2.Add_Dash(app)
    return app
