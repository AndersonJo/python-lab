'''
Created on 2014. 9. 17.

@author: a141890
'''

from cookielib import CookieJar
import codecs
import csv
import json
import urllib
import urllib2
import urlparse

# Global Settings
URL = "http://apis.daum.net/local/geo/transcoord"
CJ = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CJ))


def start():
    file = codecs.open('wifi.csv', 'r', encoding="EUC-KR")
    csv_file = csv.reader(file)
    response = []
    
    for line in csv_file:
        x, y = line[3], line[4]
        try:
            x, y = float(x), float(y)
        except:
            continue
        
        converted_data = fetch(x, y)
        response.append(converted_data)
        
    print json.dumps(response)
        
        


def fetch(x, y, from_coord='TM', to_coord='WGS84'):
    global URL, opener
    querystring = {}
    querystring['apikey'] = 'DAUM_LOCAL_DEMO_APIKEY'
    querystring['x'] = x
    querystring['y'] = y
    querystring['fromCoord'] = from_coord
    querystring['toCoord'] = to_coord
    querystring['output'] = 'json'
    
    url = URL +'?'+ urllib.urlencode(querystring) 
    response = opener.open(url)
    convered_json = json.loads(response.read())
    return {'x': convered_json['y'], 'y': convered_json['x']}
    
    
    
if __name__ == '__main__':
    start()