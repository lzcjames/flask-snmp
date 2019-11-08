from flask_sqlalchemy import SQLAlchemy
# Create database connection object
db = SQLAlchemy()

from flask import Flask

app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static')

from application import routes

from config import Config
app.config.from_object(Config)

# Connect sqlalchemy to app
db.init_app(app)

from application import models
@app.cli.command("create-db") # In console, type: flask create-db
def init_db():
   models.init_db()

    
