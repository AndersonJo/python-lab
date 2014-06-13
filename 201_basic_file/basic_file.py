# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import hashlib
import os
import unittest
import yourtest



class OSAndSysTest(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(__file__)
        self.answer1 = "7f6b2b893e5cb8f923a4e7da669557cc"
        self.answer2 = "5a326194198ba50616be2236d9e3f350"
        self.answer3 = "ef9cdad2b9976062762a39131384659f"
        
        if os.path.exists('awesome.txt'):
            os.remove(os.path.join(base_dir, 'awesome.txt'))
        
    
    
    def test_open_text(self):
        """
        python.txt 파일을 text파일로 열은후, 파일 안에 들어 있는 내용을 리턴시키세요
        """
        self.assertEqual(self.answer1, self.hash(yourtest.open_python_text()))
    
    def test_write_text(self):
        """
        awesome.txt 파일을 만드세요. 
        그 안의 내용은 python.txt의 내용이 들어가면 됩니다.
        단! 모든 "영어" 글자가 제거된체 들어가야 합니다.
        """
        answer = self.hash(yourtest.write_awesome())
        self.assertEqual(self.answer2, answer)
    
    def test_euckr(self):
        """
        korea.txt 파일을 EUC-KR 인코딩으로 저장이 되어 있다. 
        읽어서 제대로 출력 시키자
        codecs.open 사용 또는 decode를 사용한다.
        """
        answer = self.hash(yourtest.foo_euckr())
        self.assertEqual(self.answer3, answer)
        
        
    
    def hash(self, text):
        m = hashlib.md5()
        m.update(text)
        return m.hexdigest()
        
        
if __name__ == "__main__":
    unittest.main()
