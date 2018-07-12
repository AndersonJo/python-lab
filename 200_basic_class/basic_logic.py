# -*- coding:utf-8 -*-

import yourtest
import unittest
import random


class DictionaryTest(unittest.TestCase):
    
    def test_basic_class(self):
        """
        BasicTest 라는 class 를 만들어라.
        """
        basicTest = yourtest.BasicTest()
        self.assertIsInstance(basicTest, yourtest.BasicTest)
        
    def test_subclass(self):
        """
        Atom 이라는 클래스를 만들어라.
        단.. Atom은 Robot 클래스를 subclass 한다.
        """
        atom = yourtest.Atom()
        self.assertIsInstance(atom, yourtest.Atom)
        self.assertIsInstance(atom, yourtest.Robot)
    
    def test_override(self):
        """
        Robot에서 attack 과 Atom의 attack은 다르다
        """
        robot = yourtest.Robot()
        atom = yourtest.Atom()
        self.assertEqual("pow!", robot.attack())
        self.assertEqual("laser beam!", atom.attack())
    
    def test_whats_your_name(self):
        """
        로봇과 아톰의 이름은 다르다.
        """
        robot = yourtest.Robot()
        atom = yourtest.Atom()
        self.assertEqual("robot", robot.name)
        self.assertEqual("atom", atom.name)
    
        
if __name__ == "__main__":
    unittest.main()
