from flask_sqlalchemy import SQLAlchemy
from application import db
import logging as lg
from .backend.dto.Material import Material
from .backend.dto.Event import Event
from .backend.dto.Record import Record
from .backend.dto.User import User

# Material Entity 
# To create a <Material> table which is mapped <Material> DTO and is inherited from db.Model class
class Material(Material, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    ip = db.Column(db.String(128), nullable=True)
    mac = db.Column(db.String(128), nullable=False)
    interface = db.Column(db.String(128), nullable=True)
    date = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(128), nullable=True)
    community = db.Column(db.String(1024), nullable=True) 
    
    def __repr__(self):
        return '<Material %r>' % self.name 

# User Entity
# To create a <User> table which is mapped <User> DTO and is inherited from db.Model class
class User(User, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=True)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.login 

# Event Entity
# To create a <Event> table which is mapped <Event> DTO and is inherited from db.Model class
class Event(Event, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    request = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.String(128), nullable=False)
    info = db.Column(db.String(256), nullable=True)
    
    def __repr__(self):
        return ("["+self.level+"] | "+self.name+" | "+self.request+" | "+self.timestamp+" | "+self.info+" | ") 

# Record Entity
# To create a <Record> table which is mapped <Record> DTO and is inherited from db.Model class
class Record(Record, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    materialname = db.Column(db.String(128), nullable=True)
    ifname = db.Column(db.String(128), nullable=True)
    status = db.Column(db.String(64), nullable=True)
    inoctects = db.Column(db.String(256), nullable=True)
    outoctects = db.Column(db.String(256), nullable=True)
    timestamp = db.Column(db.String(128), nullable=True)
    
    

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Material("switch A","192.168.8.185","3","4","5","6","public"))
    db.session.add(User("admin","admin",True))
    db.session.add(User("user","user",False))
    db.session.add(Material("switch B","192.168.8.114","3","4","5","6","public"))
    db.session.add(Material("switch C","2","3","4","5","6","7"))
    db.session.commit()
    lg.warning('Database initialized!')


   