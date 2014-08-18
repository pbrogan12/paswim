from pprint import pprint
import json
import sys
results = open(sys.argv[1], 'r')
event = ""
swimType = ""
result = {}
points = -1
schoolStart = 4
schoolEnd = -2
for line in results:
    if 'Points' in line:
        points = -2
        schoolEnd = -3
    if 'Event' in line.split():
        event = line.strip()
        event = ''.join(event.split()[3:])
        if result.has_key(event):
            continue
        result[event] = []
        continue
    if 'Final' in line.split() or 'Preliminaries' in line.split():
        swimType = line.strip("\n")
        continue
    try:
        int(line.split()[0])
    except:
        continue

    if 'Final' in swimType:
        try:
            if len(line.split()[0]) > 2:
                continue
        except:
            pass
        try:
            lineLength = len(line.split()) - 1
            pos = line.split()[0]
            name = line.split()[1:3]
            time = line.split()[points]
            school = line.split()[schoolStart:schoolEnd]
            result[event].append(dict(pos=str(pos),
                                  name=' '.join(name),
                                  time=str(time),
                                  school=' '.join(school)))
        except:
            pass
with open(sys.argv[1] + '.json','w') as outfile:
    json.dump(result,outfile,sort_keys=True,indent=4)
