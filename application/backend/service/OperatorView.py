from ...models import Event
from ...models import Record
from ...models import Material
import jsonpickle

class OperatorView:
    #def getText():
        # get result in format Text
    #def getGraphic():
        # get result in format graphic
    def getConf():
        dictMaterials={}
        i=0
        for m in Material.query.all():
            dictMaterial={}
            dictMaterial['id'] = m.id
            dictMaterial['name'] = m.name
            dictMaterial['ip'] = m.ip
            dictMaterial['mac'] = m.mac
            dictMaterial['interface'] = m.interface
            dictMaterial['date'] = m.date
            dictMaterial['community'] = m.community
            dictMaterials[i] = dictMaterial
            i=i+1
        return dictMaterials
    
    def exportLogRecord():
        dictRecords={}
        i=0
        for r in Record.query.all():
            dictRecord={}
            dictRecord['id'] = r.id
            dictRecord['materialname'] = r.materialname
            dictRecord['ifname'] = r.ifname
            dictRecord['status'] = r.status
            dictRecord['inoctects'] = r.inoctects
            dictRecord['outoctects'] = r.outoctects
            dictRecord['timestamp'] = r.timestamp
            dictRecords[i] = dictRecord
            i=i+1
        return dictRecords

    def getLogEvent():
        events = Event.query.all()
        return (jsonpickle.encode(events))
    
    def getLogRecord():
        records = Record.query.all()
        return (jsonpickle.encode(records ))
    
    
  


    