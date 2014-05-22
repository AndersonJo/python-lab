# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

from answers import Answers
import unittest
import yourtest


class PythonHellTest(unittest.TestCase):
    def setUp(self):
        self.answer = Answers()
        
    def test_xx38(self):
        """
        2^38
        """
        self.assertEqual(274877906944, yourtest.xx38())
        
    def test_koe(self):
        """
        k -> m
        o -> q
        e - > g
        
        이문제를 풀기전.. 모든 사람들은 2번 생각을 한다.
        """
        text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
        isCorrectAnswer = self.answer.check('level1', yourtest.koe(text))
        self.assertEqual(True, isCorrectAnswer)
        
    
    def test_find_characters(self):
        """
        글자를 인식한다는 것은 신의 은총이다.
        """
        with open('_level2_data', 'rt') as f:
            text = f.read()
        isCorrectAnswer = self.answer.check('level2', yourtest.find_characters(text))
        self.assertEqual(True, isCorrectAnswer)
            
    def test_find_characters2(self):
        """
        작은 레터하나.. 그리고 정확하게! 그 양옆을 지키는 각각 3명씩의 큰 보디가드들..
        이 작은 레터들을 찾아서 모두 합한 결과를 리턴시켜라.
        """
        with open('_level3_data', 'rt') as f:
            text = f.read()
        isCorrectAnswer = self.answer.check('level3', yourtest.small_letter_and_bodyguards(text))
        self.assertEqual(True, isCorrectAnswer)
        
        
        
if __name__ == "__main__":
    unittest.main()













