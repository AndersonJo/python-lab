# -*- coding:utf-8 -*-

import yourtest
import unittest


class BasicFunctionTest(unittest.TestCase):
    """
    기본적인 함수 사용법을 배웁니다.
    """
    
    def test_reverse_boolean(self):
        """
        True, False의 각각의 반대값을 리턴시켜라. 
        """
        self.assertEqual(True, yourtest.reverse_boolean(False))
        self.assertEqual(False, yourtest.reverse_boolean(True))
        self.assertEqual(False, yourtest.reverse_boolean(123))
        self.assertEqual(True, yourtest.reverse_boolean(0))
        self.assertEqual(True, yourtest.reverse_boolean([]))
        self.assertEqual(False, yourtest.reverse_boolean([16,23,'hello']))
        self.assertEqual(False, yourtest.reverse_boolean({'mket': True}))
        self.assertEqual(True, yourtest.reverse_boolean({}))
        
    def test_create_function(self):
        """
        Lambda 함수 또는.. Wrapper 함수를 사용하여 
        다음의 결과물을 리턴시키는 함수를 만드세요.
        """
        self.assertEqual("Chang Min", yourtest.create_function("Chang Min")())
        self.assertEqual("Max", yourtest.create_function("Max")())
        self.assertEqual("Hanna", yourtest.create_function("Hanna")())
        
    def test_calculate_mean(self):
        """
        여러개의 floating point numbers 가 arguments로 들어간다.
        mean 값을 구해라 (mean == 평균)
        리턴값은 소수점 2자리수로 반올림 시켜야한다.
        round <- 반올림시키는 함수 -> stackoverflow에서 찾아볼것. 
        """
        self.assertEqual(1.77, yourtest.calculate_mean(2.0, 4.0, 1.82, 0.332, 0.7223))
        self.assertEqual(2.03, yourtest.calculate_mean(1.0, 5.2221, 0.39, 1.2, 2.3301))
        self.assertEqual(0, yourtest.calculate_mean(0))
        self.assertEqual(2.92, yourtest.calculate_mean(1,2,3,4,5, 4.2, 1.224))
        self.assertEqual(10.5, yourtest.calculate_mean(10, 11))
    
    def test_args(self):
        """
        Arguments가 들어오는데로 모두 합한 결과값을 리턴시키는 함수를 만드세요
        """
        self.assertEqual(6, yourtest.sum_args(1,2,3))
        self.assertEqual(15, yourtest.sum_args(1,2,3,4,5))
        self.assertEqual(-3, yourtest.sum_args(0, -1, -1, -1))
        self.assertEqual(0, yourtest.sum_args())
    
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
        
    def test_lambda(self):
        """
        주어진 함수를 사용해서 값을 구하라.
        """
        self.assertEqual(13, yourtest.process(4, lambda x: x+9))
        self.assertEqual(4, yourtest.process(2, lambda x: x*2))
        self.assertEqual('he', yourtest.process('hello', lambda x: x[:2]))
        self.assertEqual(15, yourtest.process(100, lambda x: 100%17))
        
        
if __name__ == "__main__":
    unittest.main()
