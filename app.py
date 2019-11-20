from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

DEBUG = True
PORT = 8000

import models
import config


from resources.user import user
from resources.location import location

login_manager = LoginManager()

app = Flask(__name__)

app.secret_key = config.SECRET_KEY
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
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

@app.route('/')
def index():
    return 'This Is Working!'

CORS(location_api, origin=['http://localhost:3000'], supports_credentials=True)
CORS(user_api, origin=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(user_api, url_prefix='/api/v1/user')
app.register_blueprint(location_api, url_prefix='/api/v1/location')
if __name__ == '__main__':
    app.run(debug=config.DEBUG, port=config.PORT)

