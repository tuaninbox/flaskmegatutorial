from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#app = Flask(__name__)
megaapp = Flask(__name__)
megaapp.config.from_object(Config)
db = SQLAlchemy(megaapp)
migrate = Migrate (megaapp,db)

from app import routes, models