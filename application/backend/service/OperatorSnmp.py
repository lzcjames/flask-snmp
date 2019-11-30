from puresnmp import get,walk

interfaces=[]
statuses={}
octects={}
merge={}
grandmerge=[]
COMMUNITY = 'public'
# TODO: besoin arrayIf[oid1,oid2,oid3...]
IfStatus = "1.3.6.1.2.1.2.2.1.8" # ifOperStatus
IfNames =  "1.3.6.1.2.1.2.2.1.2" # ifDescr
If_OutOctets = '1.3.6.1.2.1.2.2.1.16' # ifOutOctets 




class OperatorSnmp:
    def getIfNames(ip):
       for row in walk(ip, COMMUNITY, IfNames):
            n ="%s, %s" %row
            n = n.split(',')
            name = n[1].replace("b'",'')
            name = name.replace("'",'').strip()
            interfaces.append(name)
    def getOutOctects(ip):
        i=0
        for row in walk(ip, COMMUNITY, If_OutOctets):
            o ="%s, %s" %row
            o = o.split(',')
            octect = o[1].strip()
            octects[i]=octect
            i=i+1
    def getStatuses(ip):  
        j=0
        for row in walk(ip, COMMUNITY, IfStatus):
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
    def getResultSnmp(ip):
        OperatorSnmp.getIfNames(ip)
        OperatorSnmp.getOutOctects(ip)
        OperatorSnmp.getStatuses(ip)
        for i in octects: 
            merge={"octect":octects[i],"status":statuses[i]}
            grandmerge.append(merge)
        res = dict(zip(interfaces, grandmerge))
        return res
    

