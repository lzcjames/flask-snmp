from application import db
from ...models import Event
from ...models import User
import jsonpickle
import datetime
class OperatorUser:
    def addUser(user):
        # add a user to database
        entity = User(user.login, user.password, user.admin)
        event = Event("INFO", entity.name, "ADD", time, "Ajout de l'utilisateur "+ entity.name )
        
        db.session.add(entity)
        db.session.add(event)
        db.session.commit()

        print(repr(event))
        return "OK"
    def deleteUser():
        # delete ..
        return "OK"
    def updateUser():
        # update ..
        return "OK"
    def getUser():
        # get ..
        return "OK"
    def getallUser():
        users = User.query.all()
        return (jsonpickle.encode(users))
    
    def login(login):
        user = User.query.filter_by(login=login).first_or_404()
        return user
        