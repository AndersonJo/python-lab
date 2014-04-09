#-*- encoding:utf-8 -*-
'''
Created on Apr 9, 2014

@author: a141890
'''
import re
import unittest
_ANSWERS = {
    'aaacodebbb': 1,
    'codexxcode': 2,
    'cozexxcope': 2,
    'cozfxxcope': 1,
    'xxcozeyycop': 1,
    'cozcop': 0,
    'abcxyz': 0,
    'code': 1,
    'AAcodeBBcoleCCccoreDD': 3,
    'AAcodeBBcoleCCccorfDD': 2,
    'coAcodeBcoleccoreDD': 3,
}
      


class UnitTest(unittest.TestCase):
    
    def setUp(self):
        self.answers = _ANSWERS
        self.func = code_finder
    
    def test_all(self):
        for q, a in self.answers.items():
            returnValue = self.func(q)
            errMsg = "\nArguments: %s  \n답: %s \n당신의 답: %s"% (q, a, returnValue) 
            self.assertEqual(a, returnValue, msg=errMsg)


def code_finder(string):
    """
    여기다가 코드를 쓰세요.
    @param string (str)  
    @return (boolean) : code 를 찾아서 몇개인지 알아내세요. 단 code의 d는 어떤 문자 형식도 될 수 있습니다.
    """
    

for a in _ANSWERS:
    code_finder(a)


if __name__ =="__main__":
    unittest.main()
    