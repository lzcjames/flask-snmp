from flask_sqlalchemy import SQLAlchemy
from application import db
import logging as lg
from .backend.dto.Material import Material
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
    oids = db.Column(db.String(1024), nullable=True) # a JSONArray will be converted to String
    
    def __repr__(self):
        return '<Material %r>' % self.name 

# User Entity
#To create a <User> table which is mapped <User> DTO and is inherited from db.Model class
class User(User, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=True)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.fistname 

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Material("switch A","2","3","4","5","6","7"))
    db.session.add(User("toto","TATA",True))
    db.session.add(Material("switch B","2","3","4","5","6","7"))
    db.session.commit()
    lg.warning('Database initialized!')


   