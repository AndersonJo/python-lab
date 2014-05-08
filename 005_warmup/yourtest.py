'''
Created on May 7, 2014

@author: a141890
'''

def hello():
    return 'hello'

def square(i):
    return i**2

def sum_all(*args):
    return sum(args)

def monkey_trouble(a_smile, b_smile):
    return (a_smile == b_smile)

def sum_double(a, b):
    c = a + b
    if a == b:
        return c*2
    return c
  
def diff21(n):
    diff = abs(n-21)
    return diff * 2 if n > 21 else diff

def parrot_trouble(talking, hour):
    if talking and (hour <= 6 or hour > 20):
        return True
    return False

def makes10(a, b):
    s = a + b
    if a == 10 or b == 10 or s == 10:
        return True
    return False
