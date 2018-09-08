from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# from flask_login import LoginManager

app = Flask(__name__)

# from flask_login import LoginManager
login = LoginManager(app)
login.login_view = 'login'

# initializing config
app.config.from_object(Config)

# initializing database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# initializing flask-bootstrap
Bootstrap(app)

# init LoginManager from _flask_login extention
# login_manager = LoginManager()

from app import routes, models