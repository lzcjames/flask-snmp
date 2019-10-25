class Material:
    def __init__(self, name, ip, mac, interface, date, status, oids=[]):
        self.name = name
        self.ip = ip
        self.mac = mac
        self.interface = interface
        self.date = date
        self.status = status
        self.oids = oids
