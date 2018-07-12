# -*- coding:utf-8 -*-


import yourtest
import unittest


class BasicTuple(unittest.TestCase):
    """
    기본적인 튜플 사용법
    """
    
    def test_simple(self):
        your_answer = yourtest.simple()
        self.assertIsInstance(your_answer, tuple)
        self.assertEqual('Chang Min', your_answer[0])
        
    def test_nested1(self):
        data = ('a', 'b', 'c', 'd', ('a',), ('b',), (1, 2, 3, 100))
        self.assertEqual(100, yourtest.nested1(data))
    
    def test_nested2(self):
        data = (1, 2, (23, 'a', 'b', ('hello', 'on', ('python', 'chang min', 'awesome', ('haha',)))))
        self.assertEqual('haha', yourtest.nested2(data))
        
    def test_multiple_return(self):
        a, b, c, d = yourtest.multiple_return()
        self.assertEqual(a, 'Chang Min')
        self.assertEqual(b, 'is')
        self.assertEqual(c, 'AWEsoME!')
        self.assertEqual(d, '.. hehe!')
    
    def test_swap(self):
        self.assertEqual(('a', 'b'), yourtest.swap('b', 'a'))
        self.assertEqual((20, 10), yourtest.swap(10, 20))
        self.assertEqual(('EXpert', ''), yourtest.swap('', 'EXpert'))
        self.assertEqual((None, 'foo'), yourtest.swap('foo',))
        self.assertEqual((None, None), yourtest.swap())
        
    def test_sum_all(self):
        self.assertEqual(15, yourtest.sum_all(1,2,3,4,5))
        self.assertEqual(3600, yourtest.sum_all(100, 200, 300, 1000, 2000))
        self.assertEqual(10.2215, yourtest.sum_all(1.23, 4.22, 4.1123, .23, .4292))
        self.assertEqual(6, yourtest.sum_all(1, 2, 3))
        self.assertEqual(0, yourtest.sum_all())
    
    def test_index(self):
        """
        the first argument is the start index number
        the other arguments can be assumed to be a series of data like tuple.
        """
        self.assertEqual(('c', 'd', 'e'), yourtest.partial_index(2, 'a', 'b', 'c', 'd', 'e'))
        self.assertEqual((6, 7, 8, 9), yourtest.partial_index(5, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    
    def test_count(self):
        """
        Counts the first arguemnt in the rest of the arguemnts
        """
        self.assertEqual(2, yourtest.count('foo', 'python', 'foo', 'foo', 'battle'))
        self.assertEqual(5, yourtest.count(5, 1, 2, 3, 2, 5, 5, 2, 5, 5, 2, 5, 100, 200))
        self.assertEqual(1, yourtest.count('a', 'b', 'a', 'b', 'c'))
        self.assertEqual(0, yourtest.count('nothing'))
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()
