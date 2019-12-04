from application import db
from ...models import Event
from ...models import Material
import jsonpickle
import datetime

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

class OperatorMaterial:

    def add(jsonObject):
        dto = jsonpickle.decode(jsonObject)
        entity = Material(dto.name, dto.ip, dto.mac, dto.interface, dto.date, dto.community)
        event = Event("INFO", entity.name, "ADD", time, "Supprimer le matériel "+ entity.name )
        
        db.session.add(entity)
        db.session.add(event)
        db.session.commit()

        print(repr(event))
        return "OK"

    def delete(rowid):
        entity = Material.query.filter_by(id=rowid).one()
        event = Event("WARN", entity.name, "DELETE", time, "Supprimer le matériel "+ entity.name )
        
        db.session.delete(entity)
        db.session.add(event)
        db.session.commit()

        print(repr(event))
        return "OK"

    def update(jsonObject,id):
        newDto = jsonpickle.decode(jsonObject)
        dto = Material.query.get(id)
        event = Event("INFO", newDto.name, "UPDATE", time, "Mettre à jour le matériel "+ newDto.name )

        dto.name = newDto.name
        dto.ip = newDto.ip
        dto.mac = newDto.mac
        dto.interface = newDto.interface
        dto.date = newDto.date
        dto.community = newDto.community

        db.session.merge(dto)
        db.session.add(event)

        print(repr(event))
        db.session.commit()
        return "OK"

    def get(name):
        material = Material.query.filter_by(name=name).first_or_404()
        return material

    def getAll():
        materials = Material.query.all()
        return (jsonpickle.encode(materials))
        