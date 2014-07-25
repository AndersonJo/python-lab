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
import codecs



class OSAndSysTest(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(__file__)
        self.awesome_path = os.path.join(base_dir, 'awesome.txt')
        
        self.answer1 = "64258084ba1c0e33e62234cd24ba4da7"
        self.answer2 = "4a5ebbc74252c0265c202237af0c427b"
        self.answer3 = "ef9cdad2b9976062762a39131384659f"
        
        if os.path.exists(self.awesome_path):
            os.remove(self.awesome_path)
    
    def test_open_text(self):
        """
        python.txt 파일을 text파일로 열은후, 파일 안에 들어 있는 내용을 리턴시키세요
        codecs를 사용해야 합니다.
        """
        self.assertEqual(self.answer1, self.hash(yourtest.open_python_text()))
    
    def test_write_text(self):
        """
        python.txt 파일을 읽은 후
        모든 영어를 제거한뒤 awesome.txt에 저장하세요
        그리고 저장한 내용을 리턴시키세요
        """
        answer = self.hash(yourtest.write_awesome())
        if not os.path.exists(self.awesome_path):
            self.assert_('You need to make awesome.txt')
        self.assertEqual(self.answer2, answer)
    
    def test_euckr(self):
        """
        korea.txt 파일을 EUC-KR 인코딩으로 저장이 되어 있다. 
        읽어서 제대로 출력 시키자
        decode를 사용한다.
        """
        answer = self.hash(yourtest.foo_euckr())
        self.assertEqual(self.answer3, answer)
        
    def hash(self, text):
        m = hashlib.md5()
        m.update(text)
        return m.hexdigest()
        
        
if __name__ == "__main__":
    unittest.main()
