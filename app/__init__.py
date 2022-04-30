#Building the brains of the app
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

app = Flask(__name__)

def create_app(config_name):

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    return app