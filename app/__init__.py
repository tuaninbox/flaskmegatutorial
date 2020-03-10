from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#app = Flask(__name__)
megaapp = Flask(__name__)
<<<<<<< HEAD
megaapp.config.from_object(Config)
db = SQLAlchemy(megaapp)
migrate = Migrate (megaapp,db)
login = LoginManager(megaapp)
=======
>>>>>>> 30213821a289cdfe467137d6d5a99e7f3a218aeb

from app import routes, models