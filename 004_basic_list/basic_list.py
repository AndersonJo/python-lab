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
    
    def test_first_last6(self):
        """
        6이라는 숫자가 주어진 리스트안의 첫번째 또는 마지막에 오면 True를 리턴시켜라
        """
        self.assertEqual(True, yourtest.first_last6([1, 2, 6]))
        self.assertEqual(True, yourtest.first_last6([6, 1, 2, 3]))
        self.assertEqual(False, yourtest.first_last6([13, 6, 1, 2, 3]))
        self.assertEqual(True, yourtest.first_last6([13, 6, 1, 2, 6]))
        self.assertEqual(False, yourtest.first_last6([3, 2, 1]) )
        self.assertEqual(False, yourtest.first_last6([3, 6, 1]))
        self.assertEqual(True, yourtest.first_last6([3, 6]))
        self.assertEqual(True, yourtest.first_last6([6]))
        self.assertEqual(False, yourtest.first_last6([3]) )
        self.assertEqual(True, yourtest.first_last6([5, 6]))
        self.assertEqual(False, yourtest.first_last6([5, 5]))
        self.assertEqual(True, yourtest.first_last6([1, 2, 3, 4, 6]))
        self.assertEqual(False, yourtest.first_last6([1, 2, 3, 4]) )
        
    def test_same_first_last(self):
        """
        주어진 리스트의 길이가 1이상이고, 
        첫번째 그리고 마지막 Element의 값이 동일하다면 True를 리턴시켜라
        """
        self.assertEqual(False, yourtest.same_first_last([1, 2, 3]))
        self.assertEqual(True, yourtest.same_first_last([1, 2, 1]))
        self.assertEqual(True, yourtest.same_first_last([7]))
        self.assertEqual(False, yourtest.same_first_last([]))
        self.assertEqual(True, yourtest.same_first_last([1, 2, 3, 4, 5, 1]))
        self.assertEqual(False, yourtest.same_first_last([1, 2, 3, 4, 5, 13]))
        self.assertEqual(True, yourtest.same_first_last([13, 2, 3, 4, 5, 13]))
        self.assertEqual(True, yourtest.same_first_last([7, 7]) )
    
    def test_common_end(self):
        """
        두개의 리스트의 가장 맨앞 또는 맨뒤의 아이템이 동일하다면
        True를 리턴시키는 함수를 만들어라.
        """
        self.assertEqual(True, yourtest.common_end([1, 2, 3], [7, 3]))
        self.assertEqual(False, yourtest.common_end([1, 2, 3], [7, 3, 2]))
        self.assertEqual(True, yourtest.common_end([1, 2, 3], [1, 3]))
        self.assertEqual(True, yourtest.common_end([1, 2, 3], [1]))
        self.assertEqual(False, yourtest.common_end([1, 2, 3], [2]))
                         
    def test_rotate_left3(self):
        """
        숫자 3개가 들어있는 리스트가 주어진다. 
        우리는 이 리스트의 아이템들이 왼쪽으로 1칸씩 이동하길 원한다.
        가장 왼쪽에 있는 아이템은 사라지지 않고 끝으로 이동하게 된다.
        """
        self.assertEqual([2, 3, 1], yourtest.rotate_left3([1, 2, 3]))
        self.assertEqual([11, 9, 5], yourtest.rotate_left3([5, 11, 9]))
        self.assertEqual([0, 0, 7], yourtest.rotate_left3([7, 0, 0]))
        self.assertEqual([2, 1, 1], yourtest.rotate_left3([1, 2, 1]))
        self.assertEqual([0, 1, 0], yourtest.rotate_left3([0, 0, 1]))
    
    def test_has23(self):
        """
        주어진 리스트안에 2 또는 3이 존재한다면..
        True를 리턴시켜라.
        """
        self.assertEqual(True, yourtest.has23([2, 5]))
        self.assertEqual(True, yourtest.has23([4, 3]))
        self.assertEqual(False, yourtest.has23([4, 5]))
        self.assertEqual(True, yourtest.has23([2, 2]))
        self.assertEqual(True, yourtest.has23([3, 2]))
        self.assertEqual(True, yourtest.has23([3, 3]))
        self.assertEqual(False, yourtest.has23([7, 7]))
        self.assertEqual(True, yourtest.has23([3, 9]))
        self.assertEqual(False, yourtest.has23([9, 5]))
        
    def test_make_ends(self):
        """
        주어진 리스트의 첫번째와 마지막의 엘러먼트만 있는 리스트를 리턴시켜라
        """
        self.assertEqual([1, 3], yourtest.make_ends([1, 2, 3]))
        self.assertEqual([1, 4], yourtest.make_ends([1, 2, 3, 4]))
        self.assertEqual([7, 2], yourtest.make_ends([7, 4, 6, 2]))
        self.assertEqual([1, 3], yourtest.make_ends([1, 2, 2, 2, 2, 2, 2, 3]))
        self.assertEqual([7, 4], yourtest.make_ends([7, 4]))
        self.assertEqual([7, 7], yourtest.make_ends([7]))
        self.assertEqual([5, 9], yourtest.make_ends([5, 2, 9]))
        self.assertEqual([2, 1], yourtest.make_ends([2, 3, 4, 1]))
        
    def test_append(self):
        """
        주어진 parameters 를 리스트로 만들어서 리턴시키는 함수를 만들어라
        단 모든 반환되는 리스트에는, 마지막 2번째 자리에 "foo"가 있어야 한다
        """
        self.assertEqual([1,2,3,'foo',4], yourtest.append(1,2,3,4))
        self.assertEqual(['foo', 'banana'], yourtest.append('banana'))
        self.assertEqual(['foo'], yourtest.append())
        self.assertEqual(['mket', 'nosql', 'python', 'foo', 'mongodb'], 
                         yourtest.append('mket', 'nosql', 'python', 'mongodb'))
    
    def test_count_hi(self):
        """
        주어진 리스트안에 "hi" 가 몇개인지 세어보자.
        """
        self.assertEqual(1, yourtest.count_hi(['hi', 'hello']))
        self.assertEqual(0, yourtest.count_hi([]))
        self.assertEqual(3, yourtest.count_hi([1,2,3, 'xx', 'hi', 'hi', 'hi']))
        self.assertEqual(2, yourtest.count_hi(['hi', 'HI', 'ih', '', '', 'hi']))
        self.assertEqual(0, yourtest.count_hi(['hi you', 'hello hi', 'high']))
    
    def test_remove(self):
        """
        타겟이 되는 아이템을 리스트안에서 한번만 지우는 함수를 만들자.
        """
        self.assertEqual(['hi'], yourtest.remove('hi', ['hi', 'hi']))
        self.assertEqual(['apple', 'banana'], yourtest.remove('mket', ['apple', 'banana']))
        self.assertEqual(['banana'], yourtest.remove('apple', ['apple', 'banana']))
        self.assertEqual(['apple'], yourtest.remove('banana', ['apple', 'banana']))
        self.assertEqual(['mket', 'nosql', 'python', 'life', 'short'], 
                         yourtest.remove('is', ['mket', 'nosql', 'python', 'life', 'is', 'short']))
    
    def test_sort(self):
        self.assertEqual([1, 2, 5, 12, 50, 1000], yourtest.sort([5,12,2,1,1000, 50]))
        self.assertEqual(['apple', 'can', 'dream', 'www', 'yellow'], 
                         yourtest.sort(['yellow', 'dream', 'can', 'www', 'apple',]))
        self.assertEqual([], yourtest.sort([]))
        self.assertEqual([1, 5, 1000, 'a', 'd', 'f'], yourtest.sort(['a', 1, 'd', 5, 'f', 1000]))
        

if __name__ == "__main__":
    unittest.main()
