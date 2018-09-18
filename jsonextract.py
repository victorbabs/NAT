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

print(connsuniquecountpertime)



unique_ip_port_count_details = {}
