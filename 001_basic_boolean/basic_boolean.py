# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import yourtest
import unittest


class BasicBoolean(unittest.TestCase):
    """
    기본적인 boolean 사용법
    """
    
    def test_reverse_boolean(self):
        """
        반대가 되는 boolean값을 리턴시켜라
        """
        self.assertEqual(True, yourtest.reverse_boolean(False))
        self.assertEqual(False, yourtest.reverse_boolean(True))
        
    def test_crocodile(self):
        """
        두마리의 악어를 기르고 있다.
        두마리의 악어가 모두 배가 고프다면 서로 싸울것이고 문제가 생긴다.
        문제가 생겼는지 알아보는 함수를 만들자.
        """
        self.assertEqual(False, yourtest.crocodile(False, False))
        self.assertEqual(False, yourtest.crocodile(False, True))
        self.assertEqual(False, yourtest.crocodile(True, False))
        self.assertEqual(True, yourtest.crocodile(True, True))
        
    def test_machine_check(self):
        """
        도너츠 기계 4대를 운영중이다.
        잔고장이 많은 이 기계들은 가끔씩 고장이 난다.
        단 한대라도 고장이 나면 수리공을 불러야 한다.
        고장이 났는지 안났는지 알아보는 함수를 만들자.
        True = 고장났음
        """
        self.assertEqual(False, yourtest.machine_check(False, False, False, False))
        self.assertEqual(True, yourtest.machine_check(False, True, False, False))
        self.assertEqual(True, yourtest.machine_check(False, True, False, True))
        self.assertEqual(True, yourtest.machine_check(False, False, False, True))
        self.assertEqual(True, yourtest.machine_check(False, False, True, False))
        self.assertEqual(True, yourtest.machine_check(True, True, True, True))
        
        
        
        
if __name__ == "__main__":
    unittest.main()
