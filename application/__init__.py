from flask import Flask

from application import routes

from . import models
from config import Config

app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static')
app.config.from_object(Config)

# Connect sqlalchemy to app
models.db.init_app(app)

@app.cli.command()
def init_db():
   models.init_db()