# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import os
import random
import unittest
import yourtest


class DictionaryTest(unittest.TestCase):
    
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        self.TEMP_TEXT_PATH = os.path.join(self.BASE_DIR, )
    
    def test_basic_write(self):
        pass
        

        
if __name__ == "__main__":
    unittest.main()
