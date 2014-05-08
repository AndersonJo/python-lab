# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import yourtest
import unittest


class WarmupTest(unittest.TestCase):
    
    def test_hello(self):
        """
        hello 를 리턴시키는 함수를 만드세요
        """
        self.assertEqual("hello", yourtest.hello())
    
    def test_double(self):
        """
        주어진 값 (parameter)에 곱하기 2를 하는 함수를 만드세요
        """
        self.assertEqual(4, yourtest.double(2))
        self.assertEqual("hihi", yourtest.double("hi"))
        self.assertEqual(16, yourtest.double(8))
        self.assertEqual(10, yourtest.double(5))
        self.assertEqual("skrillexskrillex", yourtest.double("skrillex"))
    
        
if __name__ == "__main__":
    unittest.main()
