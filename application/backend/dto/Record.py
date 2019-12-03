class Record:
    def __init__(self, level=None, materialname=None, ifname=None, status=None, inoctects=int, outoctects=int, timestamp=None):
        self.materialname = materialname
        self.ifname = ifname
        self.status = status
        self.inoctects = inoctects
        self.outoctects = outoctects
        self.timestamp = timestamp
