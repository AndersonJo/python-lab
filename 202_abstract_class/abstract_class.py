# -*- coding:utf-8 -*-


import yourtest
import unittest
import random


class AbstractClassTest(unittest.TestCase):
    
    def test_basic(self):
        """
        from abc import abstractmethod, ABCMeta
        를 이용해서 abstract class 를 만들어라
        
        Company 클래스에는 valuation 함수가 반드시 있어야 한다.
        """
        self.assertTrue(hasattr(yourtest.Company, 'valuation'))
        with self.assertRaises(TypeError):
            yourtest.Company()
    
    def test_abstract_method(self):
        """
        Company를 subclass하는 Samsung 회사를 만들어라
        """
        samsung = yourtest.Samsung()
        self.assertEqual(1000, samsung.valuation())
        
        
        
        
    
if __name__ == "__main__":
    unittest.main()
