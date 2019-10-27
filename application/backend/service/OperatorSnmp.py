class OperatorSnmp:

    def getResultSnmp(hostname, oid):
        command = 'snmpget -v 2c -c demopublic '+' '+hostname+' '+oid
        return '2341 octets'

