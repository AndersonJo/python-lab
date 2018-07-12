# -*- coding:utf-8 -*-

import yourtest
import unittest
import random


class OperatorOverloadingTest(unittest.TestCase):
    """
    순서대로 문제를 풀어야 함
    """
    
    def test_str(self):
        """
        Number 클래스를 만든다.
        __str__, __unicode__ 메소드를 구현해라.
        """
        number = yourtest.Number(number=10)
        self.assertEqual(u"10", unicode(number))
        self.assertEqual(u"10", str(number))
    
    def test_plus(self):
        """
        더하기 
        * __add__ 를 사용한다
        """
        number = yourtest.Number(number=10)
        another = yourtest.Number(number=10)
        self.assertEqual(20, number + 10)
        self.assertEqual(20, number +  another)
        self.assertEqual(20, another + number)
        
    def test_getitem(self):
        """
        곱하기를 한다.
        * __getitem__(self, value) 를 사용한다.
        """
        print 'test_getitem'
        number = yourtest.Number(number=10)
        self.assertEqual(100, number[10])
        self.assertEqual(50, number[5])
        self.assertEqual(0, number[0])
        self.assertEqual(-130, number[-13])
    
    def test_slice(self):
        """
        * __getitem__(self, value) 를 사용한다.
        이때 value는 int값이 아닌 slice를 받는다. 
        """
        number = yourtest.Number(123456789)
        self.assertEqual("123", number[:3])
        self.assertEqual("987654321", number[::-1])
        
    def test_iter(self):
        """
        iterable로 만들자.
        이때 1부터 주어진 값까지 iterate하게 만든다.
        1 --> 2 --> 3 --> 4 --> ... --> n
        * __iter__, next 메소드를 사용한다.
        
        가장먼저 __iter__를 사용하고, __iter__가 없으면
        __getitem__을 사용하게 된다.
        
        멈추기 위해서는, StopIteration 에러를 사용한다
        """
        total = 0
        number = yourtest.Number(number=17)
        for i in number:
            total += i
        
        self.assertEqual(153, total)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], list(number))
        
    def test_contains(self):
        """
        주어진 값(n)의 범위는 n을 기준으로 +- 10이다.
        예를 들어서 n값이 100이면.. 
        90부터 110까지 이다.
        * __contains__(self, value) 를 사용한다.
        """
        number = yourtest.Number(number=100)
        self.assertEqual(True, 100 in number)
        self.assertEqual(True, 90 in number)
        self.assertEqual(True, 105 in number)
        self.assertEqual(True, 110 in number)
        self.assertEqual(True, 91 in number)
        self.assertEqual(False, 0 in number)
        self.assertEqual(False, -10 in number)
        self.assertEqual(False, 89 in number)
        self.assertEqual(False, 111 in number)
        self.assertEqual(False, 458896434 in number)
        
    def test_getattr(self):
        """
        __getattr__은 없는 attribute를 잡을때 실행이된다.
        """
        
        number = yourtest.Number(number=100)
        with self.assertRaises(AttributeError):
            number.nothing
        self.assertEqual("Your potential is limitless", number.maximum)
        
    def test_lt_gt_eq_ne(self):
        """
        less than, greater than, equal, not equal
        * __lt__(self, other), __gt__(self, other), __eq__(self, other), __ne__(self, other)
        를 사용한다.
        """
        a = yourtest.Number(number=100)
        b = yourtest.Number(number=10)
        c = yourtest.Number(number=5)
        d = yourtest.Number(number=10)
        e = yourtest.Number(number=100)
        self.assertEqual(True, a > b)
        self.assertEqual(False, a < b)
        self.assertEqual(True, c < d)
        self.assertEqual(False, c > d)
        self.assertEqual(False, a == b)
        self.assertEqual(True, a == e)
        self.assertEqual(True, a != b)
        
    def test_call(self):
        """
        __call__(self) 를 사용한다
        """
        a = yourtest.Number(10)
        b = yourtest.Number(5)
        c = yourtest.Number(-23)
        
        self.assertEqual("10 is awesome", a())
        self.assertEqual("5 is awesome", b())
        self.assertEqual("-23 is awesome", c())
        
    def test_context_manager(self):
        """
        Context Manager 는 시작과 끝을 맺을수 있다.
        __enter__(self), __exit__(self, type, value, traceback) 로 구현한다.
        
        여기서는.. with statement 안에서 여러가지 연산을 하더라도..
        with를 빠져나오면.. 원래의 값으로 돌아오도록 만든다.
        """
        a = yourtest.Number(10)
        b = yourtest.Number(5)
        
        with b as t:
            t += 10
            self.assertEqual(15, t.number)
        self.assertEqual(5, b.number)
        
        with a as h:
            h += 10
            self.assertEqual(20, h.number)
        self.assertEqual(10, a.number)
        
        
        
        
        
        
        
        
        
        
    
if __name__ == "__main__":
    unittest.main()
