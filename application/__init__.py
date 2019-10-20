from flask import Flask

app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static')
#app.config.from_object(config.Config)
from application import routes

from config import Config
app.config.from_object(Config)
from . import models

# Connect sqlalchemy to app
models.db.init_app(app)

@app.cli.command("create-db") # In cli, type: flask create-db
def init_db():
   models.init_db()