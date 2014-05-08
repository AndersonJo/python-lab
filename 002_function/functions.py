# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import yourtest
import unittest


class BasicFunctionTest(unittest.TestCase):
    """
    기본적인 함수 사용법을 배웁니다.
    """
    
    def test_args(self):
        """
        Arguments가 들어오는데로 모두 합한 결과값을 리턴시키는 함수를 만드세요
        """
        self.assertEqual(6, yourtest.sum_args(1,2,3))
        self.assertEqual(15, yourtest.sum_args(1,2,3,4,5))
        self.assertEqual(-3, yourtest.sum_args(0, -1, -1, -1))
        self.assertEqual(0, yourtest.sum_args())
    
    def test_kwargs(self):
        """
        in 또는 not__in 을 구별하는 함수를 만들어라. 
        예를 들어서
        has_kwargs(apple__in=['apple', 'banana']) 
        에는.. apple이 주어진 리스트안에 존재하기 때문에 
        {'apple': True} 를 리턴시킨다.
        """
        self.assertEqual({'apple': True}, yourtest.has_kwargs(apple__in=['apple', 'banana']))
        self.assertEqual({'apple': False}, yourtest.has_kwargs(apple__not_in=['apple', 'banana']))
        self.assertEqual({'apple': False, 'banana':False}, yourtest.has_kwargs(apple__not_in=['apple', 'banana'], banana__in=['abc']))
        self.assertEqual({}, yourtest.has_kwargs())
        self.assertEqual({'monkey': False}, yourtest.has_kwargs(monkey__in=['shark', 'squid', 'fish']))
        
    def test_guess(self):
        """
        추측놀이를 해보자. 
        answer가 되는 숫자가 있고, 맞을것이라 추측되는 여러개의 숫자들을 함수가 받는다. 
        만약 추측되는 숫자안에 answer가 있다면 True 를 리턴한다.
        """
        self.assertEqual(True, yourtest.guess(1,2,3,4,5, answer=4))
        self.assertEqual(True, yourtest.guess(100, 'abc', 'banana', 'foo', answer='foo'))
        self.assertEqual(False, yourtest.guess('hello', 'foo', answer='mentos'))
        self.assertEqual(False, yourtest.guess('sigma-x', answer='sigma-y'))
        self.assertEqual(True, yourtest.guess('mongo', 'sql', 'cassandra', 'nosql', answer='nosql'))
        
        
if __name__ == "__main__":
    unittest.main()
