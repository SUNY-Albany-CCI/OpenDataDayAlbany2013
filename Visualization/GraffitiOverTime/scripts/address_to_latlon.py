import json
import sys
import urllib2
import datetime

file = open("../server/static/data/nyc-graffiti.js")
info = json.load(file)

# Format for google geocoding api
# http://maps.google.com/maps/api/geocode/json?
#        address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=false
count = 0

withcoords = []

querybase = "http://maps.google.com/maps/api/geocode/json?address="
print len(info["data"])
for adata in info["data"]:
    print count
    if count < 300:
        count = count + 1
        continue
    words = adata[8].split()
#    count2 = 0
#    for aword in adata:
#        print count2, ":  ", aword
#        count2 = count2 + 1
    number = words[0]
    addr = number + ",+" + '+'.join(words[1:])
    query = querybase + addr + ',+' + adata[9].replace(" ", '+') + ",+New+York+City,+NY&sensor=false"
    print count, ') ', 'Fetching ', query
    responsetext = urllib2.urlopen(query)

    try:
        response = json.loads(responsetext.read())
        addr = response["results"][0]["formatted_address"]
        lat = response["results"][0]["geometry"]["location"]["lat"]
        lng = response["results"][0]["geometry"]["location"]["lng"]
    except:
        print response
        break
    created = datetime.datetime.fromtimestamp(int(adata[5])).strftime('%d-%b-%Y %H:%M')
    updated = datetime.datetime.fromtimestamp(int(adata[13])).strftime('%d-%b-%Y %H:%M')
    try:
        closed = datetime.datetime.fromtimestamp(int(adata[16])).strftime('%d-%b-%Y %H:%M')
    except:
        closed = datetime.datetime.now().strftime('%d-%b-%Y %H:%M')

    # [19]
    adata.append(addr)
    # [20]
    adata.append(lat)
    # [21]
    adata.append(lng)
    # [22]
    adata.append(created)
    adata.append(updated)
    adata.append(closed)

    withcoords.append(adata)
    count = count + 1
    if count > 2000:
        break

fileout = open("../server/static/data/withcoords.js", "w+")
json.dump(withcoords, fileout)
