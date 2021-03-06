from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

from job_spooder import routes, models
