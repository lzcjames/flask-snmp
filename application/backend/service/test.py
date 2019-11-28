from puresnmp import get,walk

interfaces=[]
statuses={}
octects={}
merge={}
grandmerge=[]
i=0
j=0
IP = "192.168.8.134"
COMMUNITY = 'public'

IfStatus = "1.3.6.1.2.1.2.2.1.8" # ifOperStatus
IfNames =  "1.3.6.1.2.1.2.2.1.2" # ifDescr
If_OutOctets = '1.3.6.1.2.1.2.2.1.16' # ifOutOctets 
If1_OutOctets = '1.3.6.1.2.1.2.2.1.16.1'
result = get(IP, COMMUNITY, If1_OutOctets)
print('''Get Result:
    Type: %s
    repr: %s
    str: %s
    ''' % (type(result), repr(result), result))

for row in walk(IP, COMMUNITY, IfNames):
    n ="%s, %s" %row
    n = n.split(',')
    name = n[1].replace("b'",'')
    name = name.replace("'",'').strip()
    interfaces.append(name)
print(interfaces)

for row in walk(IP, COMMUNITY, If_OutOctets):
    o ="%s, %s" %row
    o = o.split(',')
    octect = o[1].strip()
    octects[i]=octect
    i=i+1
print (octects) 



for row in walk(IP, COMMUNITY, IfStatus):
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

print(statuses)

for i in octects:
    
    merge={"octect":octects[i],"status":statuses[i]}
    grandmerge.append(merge)
print (grandmerge)

D = dict(zip(interfaces, grandmerge))
print (D)
    