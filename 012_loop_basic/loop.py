# -*- coding:utf-8 -*-

import random
import unittest
import yourtest




class LoopTest(unittest.TestCase):
    
    def test_til_end(self):
        """
        주어진 값까지의 1부터 모두 더한 값을 리턴시키는 함수를 만들어라.
        단. 0으로 끝나는 숫자는 모두 제외시킨다.
        """
        self.assertEqual(15, yourtest.prime_numbers(5))
        self.assertEqual(45, yourtest.prime_numbers(10))
        self.assertEqual(4500, yourtest.prime_numbers(100))
        self.assertEqual(0, yourtest.prime_numbers(0))
        self.assertEqual(0, yourtest.prime_numbers(-10))
        self.assertEqual(0, yourtest.prime_numbers(-100))
        self.assertEqual(4431859920, yourtest.prime_numbers(99239))
    
    
    def test_basic_forloop(self):
        """
        주어진 object를 for문으로 돌려서..
        결과값을 list로 리턴하여라.
        """
        self.assertEqual([1,2,3,4,5], yourtest.basic_forloop([1,2,3,4,5].__iter__()))
        self.assertEqual(['a', 'b', 'c'], yourtest.basic_forloop(['a', 'b', 'c'].__iter__()))
        self.assertEqual([], yourtest.basic_forloop([].__iter__()))
        
    def test_generator(self):
        """
        a부터 z까지 리턴시키는 generator를 만들어라
        """  
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
               'u', 'v', 'w', 'x', 'y', 'z']
        for index, alphabet in enumerate(yourtest.a_to_z()):
            self.assertEqual(abc[index], alphabet)
        
    def test_calculator(self):
        """
        사용자에게서 숫자들을 받는 함수를 만들어라. 
        사용자가 숫자들을 넣을때마다..
        
        Total : x값 
        
        이 출력이 되어야 한다.
        또한 'q' 라고 치면 더이상 사용자로부터 인풋을 받지 않으며, 
        숫자가 아닌 값을 넣었을때는.. 잘못적었다고 말해주어야한다.
        
        * raw_input 을 사용한다
        * try 문을 사용한다.
        * ValueError 에러를 잡는다.
        * while, continue, break 를 사용한다. 
        """
        yourtest.calculator()
    

        
if __name__ == "__main__":
    unittest.main()
