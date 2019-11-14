class Material:
    def __init__(self, name, ip, mac, interface, date, status, oids=[]):
        self.name = name
        self.ip = ip
        self.mac = mac
        self.interface = interface
        self.date = date
        self.status = status
        self.oids = oids
    

    def set_name(self,name):
        self.name = name
    def set_ip(self,ip):
        self.ip = ip
    def set_mac(self,mac):
        self.mac = mac
    def set_interface(self,interface):
        self.interface = interface
    def set_date(self,date):
        self.date = date
    def set_oids(self,oids=[]):
        self.oids = oids