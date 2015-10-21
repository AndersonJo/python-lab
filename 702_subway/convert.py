# -*- coding:utf-8 -*-
'''
Created on 2014. 7. 5.

@author: a141890
'''
from multiprocessing import Process
from pprint import pprint
from threading import Thread, Lock
from time import sleep
import codecs
import csv
import json
import pyproj

korea_epsg = pyproj.Proj(init="epsg:3734")
wgs84 = pyproj.Proj(init='epsg:4326')

x, y = 198472.518, 452487.224

lock = Lock()
f = open('result.txt', 'w')

def find():
    for i in xrange(7000):
        try:
            p1 = pyproj.Proj(init="epsg:"+ str(i))
            a, b = pyproj.transform(p1, wgs84, x, y)
            a, b = float(a), float(b)
            diff = abs(abs(a) - abs(b))
            #37.554748, 126.970647
            #89.415899
            
            
            if diff >= 89 and diff <= 90 and a<b:
                print 'WOW', i, diff, a, b
                
            continue
            
        except Exception as e:
            pass

def transform(x, y, diff=0):
    a, b = pyproj.transform(korea_epsg, wgs84, x, y)
    a, b = float(a), float(b)
    if diff:
        a, b = a-diff, b-diff 
    return a, b


def convert(diff=0):
    response = []
    with open('wifi.csv', 'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            try:
                station = line[1]
                
                x = float(line[4])
                y = float(line[5])
                print x, y
                
                
                x,y = transform(x, y)
                
                response.append({'x': x, 'y': y})
            except Exception as e:
                
                pass
    return response
            

# WOW 2277 89.1418479941 -102.150996108 13.0091481139
# WOW 2279 89.7264027044 -97.0252979902 -7.29889528577
# WOW 2846 89.141847995 -102.150996109 13.0091481139
# WOW 2848 89.7264027052 -97.0252979902 -7.298895285
# WOW 2918 89.1418479941 -102.150996108 13.0091481139
# WOW 2920 89.7264027044 -97.0252979902 -7.29889528577
# WOW 3663 89.141847995 -102.150996109 13.0091481139
# WOW 3664 89.1418479941 -102.150996108 13.0091481139
# WOW 3671 89.7264027052 -97.0252979902 -7.298895285
# WOW 3672 89.7264027044 -97.0252979902 -7.29889528577



if __name__ == "__main__":
    #print find()
    print transform(198472.518,452487.224)
    print 198472.518,452487.224
    result = convert(17.0303296945)
    print result
    print json.dumps(result)
    
    pass


        
        
        
        
