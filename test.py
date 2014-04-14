# -*- encoding:utf-8 -*-
from time import sleep
from bson import objectid

with open('text', 'wt') as f:
    for i in xrange(1000):
        str(objectid())