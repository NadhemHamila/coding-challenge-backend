from flask_cors import CORS
from flask import Flask
import os

from .controllers import routes



def create_app(test_config=None):
    # create and configure the app
    with open("numbers.txt", 'r+') as f:
        f.truncate()
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.register_blueprint(routes)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


# flask --app src --debug run ### to run the application
