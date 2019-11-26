from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

import models
import config

DEBUG = True
PORT = 8000

from resources.user import user
from resources.locations import location

login_manager = LoginManager()

app = Flask(__name__)
CORS(app)

app.secret_key = config.SECRET_KEY
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userId):
    try:
        return models.User.get(models.User.id == userId)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

CORS(location, origin=['http://localhost:3000', 'http://gottagonow.heroku.app.com'], supports_credentials=True)
CORS(user, origin=['http://localhost:3000', 'http://gottagonow.heroku.app.com'], supports_credentials=True)

app.register_blueprint(user, url_prefix='/api/v1/users')
app.register_blueprint(location, url_prefix='/api/v1/locations')

f 'ON_HEROKU' in os.environ:
    print('hitting')
    models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, port=config.PORT)

