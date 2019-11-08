from application import db

class OperatorSnmp:

    def getResultSnmp(hostname, oid):
        command = 'snmpget -v 2c -c demopublic '+' '+hostname+' '+oid
        return '2341 octets'

    def add(material):
        db.session.add(material)
        db.session.commit()
        return "OK"
        