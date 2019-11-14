from application import db
from ...models import Material
import jsonpickle

class OperatorSnmp:

    def getResultSnmp(hostname, oid):
        command = 'snmpget -v 2c -c demopublic '+' '+hostname+' '+oid
        return '2341 octets'

    def add(jsonObject):
        dto = jsonpickle.decode(jsonObject)
        entity = Material(dto.name, dto.ip, dto.mac, dto.interface, dto.date, dto.status, dto.oids)
        db.session.add(entity)
        db.session.commit()
        return "OK"

    def delete(jsonObject):
        dto = jsonpickle.decode(jsonObject)
        entity = Material(dto.name, dto.ip, dto.mac, dto.interface, dto.date, dto.status, dto.oids)
        db.session.delete(entity)
        db.session.commit()
        return "OK"

    def update(jsonObject):
        dto = jsonpickle.decode(jsonObject)
        newEntity = Material(dto.name, dto.ip, dto.mac, dto.interface, dto.date, dto.status, dto.oids)
        entityToModify = Material.query.filter_by(id=entity.id).first()
        entityToModify.set_name(newEntity.name)
        
        db.session.commit()
        return redirect("/")

    def get(jsonObject):
        dto = jsonpickle.decode(jsonObject)
        entity = Material(dto.name, dto.ip, dto.mac, dto.interface, dto.date, dto.status, dto.oids)
        db.session.add(entity)
        db.session.commit()
        return "OK"
        