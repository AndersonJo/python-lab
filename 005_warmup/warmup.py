# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import yourtest
import unittest


class WarmupTest(unittest.TestCase):
    """
    기본적인 논리적 흐름을 테스트 합니다
    """
    
    def test_hello(self):
        """
        hello 를 리턴시키는 함수를 만드세요
        """
        self.assertEqual("hello", yourtest.hello())
    
    def test_square(self):
        """
        주어진 값의 제곱을 리턴시키는 함수를 만드세요.
        """
        self.assertEqual(25, yourtest.square(5))
        self.assertEqual(4, yourtest.square(-2))
        self.assertEqual(0, yourtest.square(0))
        self.assertEqual(10000, yourtest.square(100))
        self.assertEqual(9, yourtest.square(3))
        
    def test_sum(self):
        """
        불규칙적으로 주어지는 값의 모든 합을 구하세요
        *args 를 사용하세요 (tuple로 값을 받습니다)
        """
        self.assertEqual(3, yourtest.sum_all(3))
        self.assertEqual(6, yourtest.sum_all(3,2,1))
        self.assertEqual(19, yourtest.sum_all(7,14,-2))
        self.assertEqual(-3, yourtest.sum_all(-1,-2,-3,0,0,3))
        self.assertEqual(101, yourtest.sum_all(0,1,100))
        self.assertEqual(20, yourtest.sum_all(5,5,5,5))
        
        
    def test_monkey_troble(self):
        """
        우리에게는 두 마리의 원숭이가 있으며, monkey_trouble 함수는 두마리의 원숭이가 웃는지 안웃는지 나타냅니다.
        만약 두마리 모두 웃거나, 안웃으면 괜찮지만, 하나는 웃고 하나는 안 웃으면 문제가 생깁니다.
        """
        self.assertEqual(True, yourtest.monkey_trouble(True, True))
        self.assertEqual(True, yourtest.monkey_trouble(False, False))
        self.assertEqual(False, yourtest.monkey_trouble(True, False))
        self.assertEqual(False, yourtest.monkey_trouble(False, True))
         
    def test_sum_double(self):
        """
        두개의 숫자가 주어지고, 둘의 합계를 리턴시키세요. 만약 둘의 숫자가 같다면 합의 곱하기 2를 해주세요
        """
        self.assertEqual(3, yourtest.sum_double(1, 2))
        self.assertEqual(5, yourtest.sum_double(3, 2))
        self.assertEqual(-1, yourtest.sum_double(-1, 0))
        self.assertEqual(12, yourtest.sum_double(3, 3))
        self.assertEqual(0, yourtest.sum_double(0, 0))
        self.assertEqual(1, yourtest.sum_double(0, 1))
        self.assertEqual(7, yourtest.sum_double(3, 4))
        
    def test_diff21(self):
        """
        주어진값과 21과의 절대값(absolute) 차이를 리턴시키세요.
        만약 그 차이값이 21을 넘을 경우, 그 차이값에 2를 곱하세요. 
        """
        self.assertEqual(2, yourtest.diff21(19))
        self.assertEqual(11, yourtest.diff21(10))
        self.assertEqual(0, yourtest.diff21(21))
        self.assertEqual(2, yourtest.diff21(22))
        self.assertEqual(8, yourtest.diff21(25))
        self.assertEqual(18, yourtest.diff21(30))
        self.assertEqual(21, yourtest.diff21(0))
        self.assertEqual(20, yourtest.diff21(1))
        self.assertEqual(19, yourtest.diff21(2))
        self.assertEqual(22, yourtest.diff21(-1))
        self.assertEqual(23, yourtest.diff21(-2))
        self.assertEqual(58, yourtest.diff21(50))
    
    def test_parrot_trouble(self):
        """
        우리는 아주 시끄러운 앵무새 한마리를 키우고 있다. 
        parrot_trouble함수는 두개의 parameters 를 받는다. 
        첫번째는 이 앵무새가 우는지 안우는지..
        두번째는 시간이다. (0~24 사이의 시간)
        
        만약 이 앵무새가 7시 이전 또는 20시 이후에 시끄럽게 울면 분명 이웃집에서 난리가 날것이다.
        문제가 생겼는지 안생겼는지 알아보는 함수를 만들어보자 
        """
        self.assertEqual(True, yourtest.parrot_trouble(True, 6))
        self.assertEqual(False, yourtest.parrot_trouble(True, 7))
        self.assertEqual(False, yourtest.parrot_trouble(False, 6))
        self.assertEqual(True, yourtest.parrot_trouble(True, 21))
        self.assertEqual(False, yourtest.parrot_trouble(False, 21))
        self.assertEqual(False, yourtest.parrot_trouble(False, 20))
        self.assertEqual(True, yourtest.parrot_trouble(True, 23))
        self.assertEqual(False, yourtest.parrot_trouble(False, 23))
        self.assertEqual(False, yourtest.parrot_trouble(True, 20))
        self.assertEqual(False, yourtest.parrot_trouble(False, 12))
        
    def test_makes10(self):
        """
        두개의 int값 형식의 parameters 가 주어진다.
        두개중의 하나라도 10이거나 또는 그 합이 10이면 True를 return 시켜라.
        """
        self.assertEqual(True, yourtest.makes10(9, 10))
        self.assertEqual(False, yourtest.makes10(9, 9))
        self.assertEqual(True, yourtest.makes10(1, 9))
        self.assertEqual(True, yourtest.makes10(10, 1))
        self.assertEqual(True, yourtest.makes10(10, 10))
        self.assertEqual(True, yourtest.makes10(8, 2))
        self.assertEqual(False, yourtest.makes10(8, 3))
        self.assertEqual(True, yourtest.makes10(10, 42))
        self.assertEqual(True, yourtest.makes10(12, -2))
        
        

        
if __name__ == "__main__":
    unittest.main()
