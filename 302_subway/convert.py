# -*- coding:utf-8 -*-
'''
Created on 2014. 7. 5.

@author: a141890
'''
from pprint import pprint
import codecs
import json
import pyproj

p1 = pyproj.Proj(init="epsg:2192")
wgs84 = pyproj.Proj(init='epsg:4326')

x, y = 493365,1125595



for i in xrange(7000):
    for j in xrange(10000):
        try:
            p1 = pyproj.Proj(init="epsg:"+ str(i))
            wgs84 = pyproj.Proj(init='epsg:'+ str(j))
            a, b = pyproj.transform(p1, wgs84, x, y)
            c, d = int(a), int(b)
            if (c in (126, 127) and d in (37, 38)) or (d in (126, 127) and c in (37, 38)):
                print 'hahahahaha:', i, j,  b, ',', a
        except :
            pass
    

# hahahahaha: 2192 37.1614584618 , 1.15144314459
# hahahahaha: 2229 37.9719016408 , -135.204857895
# hahahahaha: 2770 37.9719016419 , -135.204857894
# hahahahaha: 2874 37.9719016408 , -135.204857895
# hahahahaha: 3066 37.2679089488 , 36.9248893893
# hahahahaha: 3497 37.9719016419 , -135.204857894
# hahahahaha: 3498 37.9719016408 , -135.204857895
# hahahahaha: 5130 58.9466173826 , 37.3411235769


def c():
    coordinations = {}
    with codecs.open(u'subway_coordination.csv', 'rt', encoding='EUC-KR') as f:
        f.readline()
        f.readline()
        for line in f:
            row_data = line.split(',')
            try:
                station = row_data[1]
                x = int(row_data[5])
                y = int(row_data[6])
                coordinations[station] = {'x': x, 'y': y}
            except Exception as e:
                continue
            
    return coordinations
        
def inout():
    response = {}
    with codecs.open(u'get_in_out.csv', 'rt', encoding='EUC-KR') as f:
        print f.readline()
        print f.readline()
        for line in f:
            row_data = line.split(',')
            station = row_data[3]
            get_in = row_data[4]
            get_out = row_data[5]
            response[station] = {'in': get_in, 'out': get_out}
    return response

def main():
    coordinations = c()
    inouts = inout()
    for station, data in coordinations.items():
        a, b = pyproj.transform(p1, wgs84, data['x'], data['y'])
        print 'xy : ', station, data['x'], data['y'], b,',', a, a-b

if __name__ == "__main__":
    # main()
    pass


        
        
        
        
