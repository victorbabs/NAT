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
    uniquedestinationtosourcemapping = {}
    for eachuniquedestinationintimerange in list(connsuniquepertime[eachtimerange]):
        uniquedestinationtosourcemapping[eachuniquedestinationintimerange] = {}
    unique_ip_port_count_details[eachtimerange] = uniquedestinationtosourcemapping


for eachtimerange in keys:
    uniqueportspertimerange = connsuniquepertime[eachtimerange]
    entriesforthattime = contents[eachtimerange]
    for eachentry in entriesforthattime:
        eachuniquedst = eachentry['dst1'] + ":" + eachentry['dport1']
        eachuniquesrc = eachentry['src1']

        try:
            unique_ip_port_count_details[eachtimerange][eachuniquedst][eachuniquesrc] += 1
        except:
            unique_ip_port_count_details[eachtimerange][eachuniquedst][eachuniquesrc] = 1

#print(unique_ip_port_count_details)

#Remove unnecessary zeros
for eachtimerange in unique_ip_port_count_details.keys():
    for eachuniquedestinationintimerange in list(unique_ip_port_count_details[eachtimerange]):
        if unique_ip_port_count_details[eachtimerange][eachuniquedestinationintimerange] == {}:
            del(unique_ip_port_count_details[eachtimerange][eachuniquedestinationintimerange])


#get total
for eachtimerange in unique_ip_port_count_details.keys():
    for eachuniquedestinationintimerange in unique_ip_port_count_details[eachtimerange]:
        count = 0
        for eachvalue in unique_ip_port_count_details[eachtimerange][eachuniquedestinationintimerange].values():
            count += int(eachvalue)
        unique_ip_port_count_details[eachtimerange][eachuniquedestinationintimerange]['Total'] = count

print (unique_ip_port_count_details)
