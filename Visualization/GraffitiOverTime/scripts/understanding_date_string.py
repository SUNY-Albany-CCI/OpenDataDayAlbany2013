import json
import sys
import urllib2
import datetime

file = open("../server/static/data/nyc-graffiti.js")
info = json.load(file)
count = 0

for adata in info["data"]:
    print adata[5]
    print adata[13]
    print adata[16]
    created = datetime.datetime.fromtimestamp(int(adata[5])).strftime('%d-%b-%Y %H:%M')
    updated = datetime.datetime.fromtimestamp(int(adata[13])).strftime('%d-%b-%Y %H:%M')
    try:
        closed = datetime.datetime.fromtimestamp(int(adata[16])).strftime('%d-%b-%Y %H:%M')
    except:
        closed = datetime.datetime.now().strftime('%d-%b-%Y %H:%M')
        print 'NOOOOOOOOOOOOOOOOO'
        pass

    print created
    print updated
    print closed

    print
    count = count + 1
    if count > 100:
        break
