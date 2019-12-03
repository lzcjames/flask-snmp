from puresnmp import get,walk
from ...models import Record
from ...models import Material
import datetime
import jsonpickle
from application import db
import os

interfaces=[]
statuses={}
inOctects={}
outOctects={}
merge={}
grandmerge=[]


# TODO: besoin arrayIf[oid1,oid2,oid3...]
IfStatuses = "1.3.6.1.2.1.2.2.1.8" # ifOperStatus
IfNames =  "1.3.6.1.2.1.2.2.1.2" # ifDescr
If_OutOctets = '1.3.6.1.2.1.2.2.1.16' # ifOutOctets 
If_InOctets = '1.3.6.1.2.1.2.2.1.10' # ifInOctets 

class OperatorSnmp:
    def initVars():
        interfaces.clear()
        statuses.clear()
        inOctects.clear()
        outOctects.clear()
        merge.clear()
        grandmerge.clear()
    

    def getIfNames(ip,community):
       for row in walk(ip, community, IfNames):
            n ="%s, %s" %row
            n = n.split(',')
            name = n[1].replace("b'",'')
            name = name.replace("'",'').strip()
            interfaces.append(name)
    
    def getInOctects(ip,community):
        i=0
        for row in walk(ip, community, If_InOctets):
            o ="%s, %s" %row
            o = o.split(',')
            inOctect = o[1].strip()
            inOctects[i]=inOctect
            i=i+1
    
    def getOutOctects(ip,community):
        i=0
        for row in walk(ip, community, If_OutOctets):
            o ="%s, %s" %row
            o = o.split(',')
            outOctect = o[1].strip()
            outOctects[i] = outOctect
            i=i+1

    def getStatuses(ip,community):  
        j=0
        for row in walk(ip, community, IfStatuses):
            t ="%s, %r" %row
            t = t.split(',')

            if "1" in t[1] :
                status = "UP"
            
            elif "2" in t[1]:
                status="DOWN"

            elif "3" in t[1]:
                status="TESTING"

            statuses[j]=status
            j=j+1

    def addRecord (result,materialname):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        for key, value in result.items():
            record = Record()
            record.materialname = materialname
            record.ifname = key
            record.timestamp = time
            for subkey, subvalue in value.items():
                if (subkey == "status"):
                    record.status = subvalue
                if (subkey == "inoctects"):
                    record.inoctects = subvalue
                if (subkey == "outoctects"):    
                    record.outoctects = subvalue
            db.session.add(record)
            db.session.commit()

    def getRecordsbyNameAndDate(materialname):
        records=[]
        lastTarget = Record.query.filter_by(materialname=materialname).order_by(Record.timestamp.desc()).first_or_404(description='No data')
        records = Record.query.filter_by(materialname=materialname,timestamp = lastTarget.timestamp).all()
        return jsonpickle.encode(records)

    def getRecordsbyNameAndIfname(materialname,ifname):
        records=[]
        records = Record.query.filter_by(materialname=materialname, ifname=ifname).all()
        return jsonpickle.encode(records)
        

    def getResultSnmp(ip,materialname,community):
        OperatorSnmp.initVars()
        OperatorSnmp.getIfNames(ip,community)
        OperatorSnmp.getInOctects(ip,community)
        OperatorSnmp.getOutOctects(ip,community)
        OperatorSnmp.getStatuses(ip,community)
       
        for i in statuses: 
            merge={"status":statuses[i],"inoctects":inOctects[i], "outoctects":outOctects[i]}
            grandmerge.append(merge)
        result = dict(zip(interfaces, grandmerge))
       
        OperatorSnmp.addRecord(result,materialname)
        
        return result

    def monitorSnmp():
        materials = Material.query.all()
        for m in materials:
            response = os.system('ping -n 1 ' + m.ip)
            if response == 0:
                OperatorSnmp.getResultSnmp(m.ip, m.name,m.community) 
        return materials
    

    
    

