# -*- coding:utf-8 -*-


import yourtest
import unittest
import random


class DecoratorTest(unittest.TestCase):
    def test_greet(self):
        '''
        You need to make a 'greet' decorator which detects the first argument and 
        if the first argument is string then add 'Hello ' to the first argument.
        '''
        
        self.assertEqual(True, hasattr(yourtest, 'greet'))
        self.assertEqual('Hello Chang Min', yourtest.name('Chang Min'))
        self.assertEqual('Hello Alice', yourtest.name('Alice'))
        self.assertEqual(123, yourtest.name(123))
        self.assertEqual([1,2,3,4,5], yourtest.name([1,2,3,4,5]))
        
    
    def test_stop_japan(self):
        """
        I just hate Japan. 
        
        * Do not decorate "japan_ok" function
        """
        japan_hater = yourtest.stop_japna(yourtest.japan_ok)
        
        self.assertEqual(['korean', 'japan'], yourtest.japan_ok('korean', 'japan'))
        self.assertEqual(['japan'], yourtest.japan_ok('japan'))
        self.assertEqual(['chinese', 'japan'], yourtest.japan_ok('chinese', 'japan'))
        
        self.assertEqual(['korean'], japan_hater('korean', 'japan'))
        self.assertEqual([], japan_hater('japan'))
        self.assertEqual(['chinese'], japan_hater('chinese', 'japan'))
        
    
    def test_counter_decorator(self):
        """
        Make a Counter decorator; it is useful when counting how many times a function has been called
        
        You need to make 'counter_decorator' decorator and attack function.
        """
        self.assertEqual(True, hasattr(yourtest, 'counter_decorator'))
        self.assertEqual(0, yourtest.attack.count)
        self.assertEqual('attack', yourtest.attack())
        self.assertEqual(1, yourtest.attack.count)
        self.assertEqual('attack', yourtest.attack())
        self.assertEqual(2, yourtest.attack.count)
        self.assertEqual('attack', yourtest.attack())
        self.assertEqual(3, yourtest.attack.count)
        
    
if __name__ == "__main__":
    unittest.main()
