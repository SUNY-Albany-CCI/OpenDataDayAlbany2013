import json

file = open("../server/data/nyc-graffiti.js")
info = json.load(file)
print info.keys()

print info["meta"].keys()

print 'Format \n######'
count = 0
for acolumn in  info["meta"]["view"]["columns"]:
    print count, acolumn["fieldName"]
    count = count + 1

print ""
