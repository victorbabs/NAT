import json


with open('output.log', 'r') as file:
    contents = file.read()
    contents = json.loads(contents)

#print(contents)

connsuniquepertime = {}
unique_ip_port = set()

keys = contents.keys()


for eachkey in keys:
    entries = contents[eachkey]
    for eachentry in entries:
        unique_ip_port.add(eachentry['dst1'] + ":" + eachentry['dport1'])

    connsuniquepertime[eachkey] = unique_ip_port

#print(connsuniquepertime)

unique_ip_port_count = {}
connsuniquecountpertime = {}

for eachkey in keys:
    entries = contents[eachkey]
    for eachentry in entries:
        try:
            unique_ip_port_count[eachentry['dst1'] + ":" + eachentry['dport1']] += 1
        except:
            unique_ip_port_count[eachentry['dst1'] + ":" + eachentry['dport1']] = 1

    connsuniquecountpertime[eachkey] = unique_ip_port_count

#print(connsuniquecountpertime)




unique_ip_port_count_details = {}
for eachtimerange in keys:
    unique_ip_port_count_details[eachtimerange] = dict.fromkeys(list(unique_ip_port), {})

print(unique_ip_port_count_details)

for eachtimerange in keys:
    #print (eachtimerange)
    uniqueportspertimerange = connsuniquepertime[eachtimerange]
    #print (uniqueportspertimerange)
    entriesforthattime = contents[eachtimerange]
    #print (len(entriesforthattime))
    for eachentry in entriesforthattime:
        #print (eachentry)
        eachuniquedst = eachentry['dst1'] + ":" + eachentry['dport1']
        eachuniquesrc = eachentry['src1'] + ":" + eachentry['sport1']
        #print(eachuniquedst, eachuniquesrc)
        try:
            unique_ip_port_count_details[eachtimerange][eachuniquedst][eachuniquesrc] += 1
            print ("An exception did not occur")
        except:
            unique_ip_port_count_details[eachtimerange][eachuniquedst][eachuniquesrc] = 1
            print ("An exception occur")

        print(unique_ip_port_count_details)