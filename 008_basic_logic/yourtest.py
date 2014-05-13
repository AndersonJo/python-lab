# -*- coding:utf-8 -*-
'''
Created on May 13, 2014

@author: a141890
'''
def gt12(x):
    return True if x > 12 else False


def process(x, func):
    return func(x)

def president_safe(who):
    if who == u"이슬람 무장단체":
        return 6
    
def is_ok(camera=False, music=False, lighting=False, just_go=False):
    if just_go:
        return True
    return  all((camera, music, lighting))

def church(day='', work=False):
    if day == 'sunday':
        return True
    
    if day == 'friday' and not work:
        return True
    return False

def economy_risk(rate, boom=False):
    if rate >= 1200 or rate <= 1000:
        if not boom:
            return True
    return False

def complicated_sum():
    pass