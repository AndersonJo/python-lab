# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''
import re
import unittest
import yourtest



class RegexBasic(unittest.TestCase):
    def test_color(self):
        """
        color 그리고 colour 단어를 찾는 것을 구현해라
        """
        self.assertNotEqual(None, yourtest.color('color'))
        self.assertNotEqual(None, yourtest.color('colour'))
        self.assertEqual(None, yourtest.color('colo'))
        self.assertEqual(None, yourtest.color('cololcolo'))
        self.assertEqual(None, yourtest.color(''))
        self.assertEqual(None, yourtest.color('olor'))
        self.assertEqual(None, yourtest.color('coloul'))
        self.assertNotEqual(None, yourtest.color('hello color'))
        self.assertNotEqual(None, yourtest.color('hello colour xx'))
        self.assertNotEqual(None, yourtest.color('collourcolorcolol'))
        self.assertNotEqual(None, yourtest.color('collolcocolcolourlcollour'))
        
    def text_winner(self):
        """
        winner 라는 글자를 잡아낸다. 단 winner!는 잡히지 말아야한다.
        """
        self.assertNotEqual(None, yourtest.winner('winner'))
        self.assertEqual(None, yourtest.winner('winner!'))
        self.assertEqual(None, yourtest.winner('winnner winne winnener winner! winneer'))
        self.assertNotEqual(None, yourtest.winner('winner! win winn er winner win'))
        self.assertNotEqual(None, yourtest.winner('winn win! winnerr! winnerw!'))
       
   
        
        
if __name__ == "__main__":
    unittest.main()
