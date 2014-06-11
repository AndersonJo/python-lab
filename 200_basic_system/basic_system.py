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


class OSAndSysTest(unittest.TestCase):
    def setUp(self):
        self.basedir = os.path.dirname(__file__)
        for d in ['test', 'foo']:
            testDir = os.path.join(self.basedir, d)
            if os.path.exists(testDir):
                os.rmdir(testDir)
            
    
    def test_get_current_working_directory(self):
        """
        현재 파이썬이 실행되는 디렉토리를 리턴시키세요
        """
        self.assertEqual(self.basedir, yourtest.getCwd())
    
    def test_mkdir(self):
        """
        test 이름을 갖은 directory를 생성시키세요
        """
        yourtest.make_test_directory()
        
        directory = os.path.join(self.basedir, "test")
        self.assertTrue(os.path.exists(directory))
        
    def test_rmdir(self):
        """
        test directory 를 삭제시키세요
        """
        self._mktest()
        yourtest.remove_test_directory()
        
        directory = os.path.join(self.basedir, "test")
        self.assertFalse(os.path.exists(directory))
        
    def test_rename(self):
        """
        test directory 이름을 foo 로 변경하세요
        """
        self._mktest()
        yourtest.rename_test_to_foo()
        
        directory = os.path.join(self.basedir, "foo")
        self.assertTrue(os.path.exists(directory))
        
    def _mktest(self):
        d = os.path.join(self.basedir, "test")
        if not os.path.exists(d):
            os.mkdir(d)
        
if __name__ == "__main__":
    unittest.main()
