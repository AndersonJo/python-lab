# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import yourtest
import unittest


class BasicFunction(unittest.TestCase):
    def test_basic(self):
        """
        3개의 arguments 를 받는 함수를 만들어라. 
        그 함수는 3개의 arguments를 모두 더한 값을 리턴시킨다.
        """
        self.assertEqual(6, yourtest.sum(1,2,3))
        self.assertEqual(9, yourtest.sum(6,3,0))
        self.assertEqual(0, yourtest.sum(0,0,0))
        self.assertEqual(-30, yourtest.sum(-100,50,20))
    
    def test_lambda(self):
        """
        주어진 값을 더블시키는 lambda 함수를 리턴시켜라
        """
        self.assertEqual("hellohello", yourtest.double('hello')())
        self.assertEqual(10, yourtest.double(5)())
        self.assertEqual(16, yourtest.double(8)())
        self.assertEqual(0, yourtest.double(0)())
        self.assertEqual('xx', yourtest.double('x')())
        
        
        
if __name__ == "__main__":
    unittest.main()
