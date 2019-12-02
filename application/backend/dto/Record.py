class Record:
    def __init__(self, level=None, materialname=None, ifname=None, status=None, inoctects=None, outoectects=None, timestamp=None):
        self.materialname = materialname
        self.ifname = ifname
        self.status = status
        self.inoctects = inoctects
        self.outoectects = outoectects
        self.timestamp = timestamp
