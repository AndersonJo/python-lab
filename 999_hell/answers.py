#-*- coding:utf-8 -*-
'''
Created on May 13, 2014

@author: a141890
'''

import pickle
import string
import hashlib

class Answers(object):
    FILE_NAME = '_answer'
    
    def __init__(self):
        pass

    def __get_answers(self):      
        text = None
        with open(Answers.FILE_NAME, 'rt') as f:
            text = pickle.load(f)
        return text
    
    def __check(self, levelName, value):
        answer = self.__get_answers()[levelName]
        
        if answer == hashlib.sha512(value).hexdigest():
            return True
        return False
    
    def check(self, levelName, value):
        return self.__check(levelName, value)
    









































# Pickle the real answers
answers= {}
answers['level1'] = "i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
answers['level2'] = 'equality'
answers['level3'] = 'linkedlist'

# 여기까지 풀었음 ..
# http://www.pythonchallenge.com/pc/def/linkedlist.php



for k, v in answers.items():
    answers[k] = hashlib.sha512(v).hexdigest()

with open('_answer', 'wt') as f:
    pickle.dump(answers, f)

print 'done'

