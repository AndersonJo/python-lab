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

class BasicFileTest(unittest.TestCase):
    
    def test_basic_decode(self):
        """
        Decode the following words
        """
        self.assertEqual(u'한글', yourtest.simple_decode('\xed\x95\x9c\xea\xb8\x80'))
        self.assertEqual(u'조창민', yourtest.simple_decode('\xec\xa1\xb0\xec\xb0\xbd\xeb\xaf\xbc'))
        self.assertEqual(u'프로페셔널', yourtest.simple_decode('\xed\x94\x84\xeb\xa1\x9c\xed\x8e\x98\xec\x85\x94\xeb\x84\x90'))
        
    def test_basic_encode(self):
        """
        Encode the following 
        """
        self.assertEqual('\xed\x95\x9c\xea\xb8\x80', yourtest.simple_encode(u'한글'))
        self.assertEqual('\xe6\x82\xa8\xe5\xa5\xbd', yourtest.simple_encode(u'您好'))
        self.assertEqual('\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf', yourtest.simple_encode(u'こんにちは'))
    
    def test_stupid_open(self):
        """
        open the "python.txt" file without codecs library
        return the first word of the third line  of the content.
        You need to decode the word with UTF-8
        """
        correct_answer = u"파이썬은"
        your_answer = yourtest.stupid_open()
        self.assertEqual(correct_answer, your_answer)
    
    def test_codecs_open(self):
        """
        Just open the "python.txt" with codecs library.
        return the content of the file
        """
        correct_answer = "7f6b2b893e5cb8f923a4e7da669557cc"
        content = yourtest.just_codecs_open()
        your_answer = self._make_hash(content)
        self.assertEqual(correct_answer, your_answer)
        
    def test_codecs_open_with_euckr(self):
        """
        Open the "korea.txt" file with codecs library.
        You may need to use 'EUC-KR' codec.
        
        Return the most frequently shown word
        """
        self.assertEqual(u'한반도', yourtest.open_euckr())
        
    def _make_hash(self, content):
        md5 = hashlib.md5()
        md5.update(content.encode('utf-8'))
        return md5.hexdigest()
        
if __name__ == "__main__":
    unittest.main()
