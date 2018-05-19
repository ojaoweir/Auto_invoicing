from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

#db object represents the database
db = SQLAlchemy(app)
#migrate represents the migration engine
migrate = Migrate(app, db)

from program import models
