'''
Created on May 13, 2014

@author: a141890
'''
import re
import string

def xx38():
    return 2**38

def koe(text):
    response = []
    answer = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
    tab = string.maketrans(string.ascii_lowercase, answer)
    return text.translate(tab)

def find_characters(text):
    text = re.sub('[^a-zA-Z]', '', text)
    return text

def small_letter_and_bodyguards(text):
    pattern = re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")
    print ''.join(re.findall(pattern, text))