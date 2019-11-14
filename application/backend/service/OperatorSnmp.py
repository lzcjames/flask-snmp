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

    def delete(rowid):
        obj = Material.query.filter_by(id=rowid).one()
        db.session.delete(obj)
        db.session.commit()
        return "OK"

    def update(jsonObject,id):
        newDto = jsonpickle.decode(jsonObject)
        dto = Material.query.get(id)

        dto.name = newDto.name
        dto.ip = newDto.ip
        dto.mac = newDto.mac
        dto.interface = newDto.interface
        dto.date = newDto.date
        dto.status = newDto.status
        dto.oids = newDto.oids

        db.session.merge(dto)
        db.session.commit()
        return "OK"
    
    def get(name):
        material = Material.query.filter_by(name=name).first_or_404()
        return material

    def getAll():
        materials = Material.query.all()
        return (jsonpickle.encode(materials))
        