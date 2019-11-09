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
        