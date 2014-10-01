# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import unittest
import yourtest




class MediumMath(unittest.TestCase):

    def test_ceil(self):
        self.assertEqual(10, yourtest.my_ceil(9.3))
        self.assertEqual(1, yourtest.my_ceil(0.2))
        self.assertEqual(-3, yourtest.my_ceil(-3.7))
        
    def test_round(self):
        self.assertEqual(0.12, yourtest.my_round(0.123568343))
        self.assertEqual(45.28, yourtest.my_round(45.2834682))
        self.assertEqual(0, yourtest.my_round(0))
        self.assertEqual(123, yourtest.my_round(123))
    
    def test_sum(self):
        """
        첫항과 말항이 주어진다. 
        이 안에 들어있는 모든 정수값을 더하라.
        
        for문을 사용하지 않는다.

        n(a+l)/2
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
        
        """
        self.assertEqual(4, yourtest.sum_odd(2))
        self.assertEqual(9, yourtest.sum_odd(3))
        self.assertEqual(225, yourtest.sum_odd(15))
        self.assertEqual(1156, yourtest.sum_odd(34))
        self.assertEqual(10000, yourtest.sum_odd(100))
        
    def test_equation1(self):
        """
        E(x**2)
        
        E = sigma
        """
        self.assertEqual(30, yourtest.equation1([1,2,3,4]))
        self.assertEqual(145, yourtest.equation1([-10, 5, 2, 4]))
        self.assertEqual(0, yourtest.equation1([]))
        
    def test_equation2(self):
        """
        Euclidean distance
        If you dont' know what it is, just google it. 
        
        sqrt(E((x-y)**2))
        
        the calculated value should be rounded to 2 decimal place
        """
        self.assertEqual(31.64, yourtest.equation2([10, 4, 20], [20, 30, 5]))
        self.assertEqual(33.67, yourtest.equation2([1,2,3], [10, 20, 30]))
        self.assertEqual(0.0, yourtest.equation2([1], [1]))
        self.assertEqual(10.0, yourtest.equation2([10], [20]))
        self.assertEqual(14.14, yourtest.equation2([20, 30], [30, 40]))
        self.assertEqual(0.0, yourtest.equation2([], []))
        






        
    def test_standard_deviation(self):
        """
        Return the sample standard deviation.
        Do not use the numpy.std function
        If you don't know what standard deviation, just google it.
        the measured value must be rounded to 4 decimal place. 
        
        s = sqrt(E(x - mean(X))**2/n-1)
        """
        self.assertEqual(2.4495,  yourtest.my_sample_std([10,4,2, 4, 7, 8, 9]))
        self.assertEqual(449.4185,  yourtest.my_sample_std([1, 100, 1000]))
        self.assertEqual(2.6458,  yourtest.my_sample_std([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        
        
    
    

if __name__ == "__main__":
    unittest.main()
