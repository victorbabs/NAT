
import time
import datetime
import json

position = 0
connspertime = {}


while True:
    with open('log', 'r') as f:
        f.seek(position, 0)
        print ('Before: ' + datetime.datetime.utcnow())
        lines = f.readlines()
        position = f.tell()
        #print (lines)
        entries = []

        for eachline in lines:
            #print (eachline)
            eachline = eachline.strip(' ').strip('\n')
            if eachline:
                fields = eachline.split()
                if fields[0] == '[NEW]':
                    if fields[1] == 'tcp':
                        protocol = fields[1]
                        state = fields[4]
                        src1 = fields[5]
                        dst1 = fields[6]
                        sport1 = fields[7]
                        dport1 = fields[8]
                        src2 = fields[10]
                        dst2 = fields[11]
                        sport2 = fields[12]
                        dport2 = fields[13]
                    elif fields[1] == 'udp':
                        protocol = fields[1]
                        state = 'N/A'
                        src1 = fields[4]
                        dst1 = fields[5]
                        sport1 = fields[6]
                        dport1 = fields[7]
                        src2 = fields[9]
                        dst2 = fields[10]
                        sport2 = fields[11]
                        dport2 = fields[12]
                    elif fields[1] == 'icmp':
                        protocol = fields[1]
                        state = 'N/A'
                        src1 = fields[4]
                        dst1 = fields[5]
                        sport1 = 'N/A'
                        dport1 = 'N/A'
                        src2 = fields[10]
                        dst2 = fields[11]
                        sport2 = 'N/A'
                        dport2 = 'N/A'
                    else:
                        protocol = 'N/A'
                        state = 'N/A'
                        src1 = 'N/A'
                        dst1 = 'N/A'
                        sport1 = 'N/A'
                        dport1 = 'N/A'
                        src2 = 'N/A'
                        dst2 = 'N/A'
                        sport2 = 'N/A'
                        dport2 = 'N/A'
                        stale = 'N/A'
                    entries.append({'protocol': protocol, 'state': state, 'src1': src1, 'dst1': dst1, 'sport1': sport1,
                                'dport1': dport1, 'src2': src2, 'dst2': dst2, 'sport2': sport2, 'dport2': dport2})
        #print(entries)

        if entries:
            connspertime[str(datetime.datetime.utcnow())] = entries

        output = open('output.log', 'w')
        output.write(json.dumps(connspertime))
        output.close()
        print ('After: ' + datetime.datetime.utcnow())

    time.sleep(1)