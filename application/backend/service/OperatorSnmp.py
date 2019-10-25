class OperatorSnmp:
    def addMaterial():
        # add a material to database
        return null
    def deleteMaterial():
        # delete ..
        return null
    def updateMaterial():
        # update ..
        return null
    def getMaterial():
        # get ..
        return null
    def getMaterials():
        # get list of ..
        return null


    def getResultSnmp(hostname, oid):
        command = 'snmpget -v 2c -c demopublic '+' '+hostname+' '+oid
        return '2341 octets'

