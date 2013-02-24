import json

file = open("../server/static/data/withcoords-300.js")
coords = json.load(file)
print len(coords)

file = open("../server/static/data/withcoords-300-71.js")
newcoords = json.load(file)

for acoord in newcoords:
    coords.append(acoord)

print len(coords)
file = open("../server/static/data/withcoords-combined.js", "w+")
json.dump(coords, file)
