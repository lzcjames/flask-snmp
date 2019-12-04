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

# schedule job    
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from .backend.service.OperatorSnmp import OperatorSnmp
from datetime import datetime
def monitor_snmp():
    res = OperatorSnmp.monitorSnmp()
    print (res)

db.app = app
scheduler = BackgroundScheduler()
scheduler.add_job(func=monitor_snmp, trigger="interval", seconds=60)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())