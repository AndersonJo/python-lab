'''
Created on 2014. 9. 18.

@author: a141890
'''
from gevent import monkey
import gevent
from cookielib import CookieJar
from pprint import pprint
import codecs
import csv
import json
import urllib
import urllib2



##############################################################################
# Settings

KEY = 'sample'  # You need to provide your Open API Key
 
##############################################################################

def retreive_seoul_wifi_data():
    """
    Retrieve the open WIFI location from Seoul Open Data
    the function will save 'wifi.csv' file.
    """
    global KEY
    seoul_wifi_url = 'http://openAPI.seoul.go.kr:8088/{key}/{type}/PublicWiFiPlaceInfo/{start}/{end}/'
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))
    
    with codecs.open('wifi.csv', 'wt', encoding="UTF-8") as f:
        wifi_csv = csv.writer(f)
        
        for page in xrange(0, 10000, 4):
            data = {}
            data['key'] = KEY
            data['type'] = 'json'
            data['service'] = 'PublicWiFiPlaceInfo'
            data['start'] = page
            data['end'] = page + 4
            
            api_url = seoul_wifi_url.format(**data)
            print page, api_url
            response = opener.open(api_url)
            content = response.read()
            
            try:
                wifis = json.loads(content)['PublicWiFiPlaceInfo']['row']
                if not wifis:
                    break
            except KeyError as e:
                print 'ERROR', content
                break
                
            
            wifis = wifis
            for wifi in wifis:
                wifi_csv.writerow(wifi.values())
                

def convert():
    """
    The location data retrieved from Seoul Open Data are using GRS80TM.
    which, of course, is not supported by the Google Map. 
    Google Map use WGS84.
    
    The function will convert the GRS80TM to WGS84 and save the convered data to 'converted_wifi.csv'
    """
    reader = csv.reader(codecs.open('wifi.csv', 'rt', encoding="UTF-8"))
    writer = csv.writer(codecs.open('converted_wifi.csv', 'wt', encoding="UTF-8"))
    
    
    for line in reader:
        x, y = line[4], line[5]
        try:
            x, y = float(x), float(y)
        except Exception as e:
            print e
            continue
        
        converted_data = _fetch(x, y)
        row = [line[0], line[1], line[2], line[3]]
        row.append(converted_data['x'])
        row.append(converted_data['y'])
    
        writer.writerow(row)
    

def _fetch(x, y, from_coord='TM', to_coord='WGS84'):
    URL = "http://apis.daum.net/local/geo/transcoord"
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))
    
    querystring = {}
    querystring['apikey'] = 'DAUM_LOCAL_DEMO_APIKEY'
    querystring['x'] = x
    querystring['y'] = y
    querystring['fromCoord'] = from_coord
    querystring['toCoord'] = to_coord
    querystring['output'] = 'json'
    
    url = URL + '?' + urllib.urlencode(querystring) 
    response = opener.open(url)
    convered_json = json.loads(response.read())
    return {'x': convered_json['y'], 'y': convered_json['x']}
    
if __name__ == '__main__':
    pass
    # retreive_seoul_wifi_data()
    convert()
