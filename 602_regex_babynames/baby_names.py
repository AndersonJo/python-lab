#-*- encoding:utf-8 -*-
'''
Created on Apr 9, 2014

@author: a141890
'''
from pprint import pprint
import pickle
import re
import unittest


_BABY_FILE_NAMES = [
    'baby1990.html',
    'baby1992.html',
    'baby1994.html',
    'baby1996.html',
    'baby1998.html',
    'baby2000.html',
    'baby2002.html',
    'baby2004.html',
    'baby2006.html',
    'baby2008.html',
]


class UnitTest(unittest.TestCase):    
    def setUp(self):
        self.func = implement
        print "*********** Unittest Start ************".center(70)
    
    def test_all(self):
        """
        response = {}
        for fileName in _BABY_FILE_NAMES:
            with open(fileName, 'r') as f:
                returnValue = self.func(f.read())
                response[fileName] = returnValue
        with open('answers.txt', 'w') as f:
            pickle.dump(response, f, protocol=pickle.HIGHEST_PROTOCOL)
        """
        answerFiles = None
        with open('answers.txt', 'rt') as answerFile:
            answerFiles = pickle.load(answerFile)
             
        for fileName in _BABY_FILE_NAMES:
            with open(fileName, 'rt') as f:
                returnValue = self.func(f.read())
            
            if type(returnValue) != dict:
                self.fail("You must return the dictionary that includes rank, male & femail Names ")
            
            answerFile = answerFiles[fileName]
            for k, v in answerFile.items():
                myValue  = returnValue[k]
                print 'Check -> %-5s, %-30s %-30s'% (k, v, myValue)
                
                if set(v) ^ set(myValue):
                    err = '*'*80 +'\n'
                    err += '%s is not the same as %s'%(v, myValue) +'\n'
                    err += '*'*80 +'\n'
                    self.fail(err)
        
        
        
        

def implement(text):
    """
    여기다가 코드를 쓰세요.
    @param text (str) : 년도별의 각각의 파일의 텍스트 값
    @return (dict) : rank를 키값으로 갖으며, value 값으로 list를 갖는 값을 리턴시키세요 
                     value 값에는.. Male Name, Female Name 이 있어야 합니다.
                     {'1': ['Male Name', 'Female Name']}
    """
    response = {}
    
    return response


if __name__ =="__main__":   
    unittest.main()
 
    