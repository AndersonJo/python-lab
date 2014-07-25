# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import random
import unittest
import yourtest




class AlgorithmTest(unittest.TestCase):
    
    def test_sum(self):
        """
        첫항과 말항이 주어진다. 
        이 안에 들어있는 모든 정수값을 더하라.
        
        for문을 사용하지 않는다.
        """
        self.assertEqual(55, yourtest.sum_all(1, 10))
        self.assertEqual(5050, yourtest.sum_all(1, 100))
        self.assertEqual(3825, yourtest.sum_all(50, 100))
        self.assertEqual(140547802020, yourtest.sum_all(1, 530184))
        self.assertEqual(0, yourtest.sum_all(-1, 1))
        self.assertEqual(0, yourtest.sum_all(0, 0))
    
    def test_sum_odd(self):
        """
        1부터 시작하여.. n값까지의 모든 odd(홀수) 값을 더하여라.
        
        n=1 : 1
        n=2 : 1+3
        n=3 : 1+3+5
        n=4 : 1+3+5+7
        
        집접 손으로 써보고 패턴을 찾아낸다.
        """
        self.assertEqual(4, yourtest.sum_odd(2))
        self.assertEqual(9, yourtest.sum_odd(3))
        self.assertEqual(225, yourtest.sum_odd(15))
        self.assertEqual(1156, yourtest.sum_odd(34))
        self.assertEqual(10000, yourtest.sum_odd(100))
        
    
    
    

        
if __name__ == "__main__":
    unittest.main()
