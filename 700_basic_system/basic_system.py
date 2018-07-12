# -*- coding:utf-8 -*-


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
                
    def test_basedir(self):
        """
        파일명이 포함된 절대주소값이 주어진다. 
        파일명을 제외한 주소를 넘겨라 
        예를 들어서
        /python/foo/haha/mket.txt 
        라는 파일은 
        /python/foo/haha
        를 넘겨야 한다.
        
        os.path 모듈안의 함수를 사용한다.
        모르면 stackoverflow 참고할것
        """
        data = {}
        data['/python/foo/haha'] = '/python/foo/haha/address.txt'
        data['/usr/local/python/pypy'] = '/usr/local/python/pypy/x.html'
        data['/'] = '/usr'
        data['/'] = '/'
        
        for k, v in data.items():
            self.assertEqual(k, yourtest.basedir(v))
            
    
    def test_get_current_working_directory(self):
        """
        현재 파이썬이 실행되는 디렉토리를 리턴시키세요
        """
        self.assertEqual(self.basedir, yourtest.get_cwd())
    
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
        
    def test_open_gedit(self):
        """
        os.popen 을 사용해서 gedit (텍스트 에디터) 를 실행시키자
        유닛 테스트가 끝나면.. 
        텍스트 에디터가 떠야 한다.
        
        os.popen 을 사용한다.
        
        """
        yourtest.open_gedit()
        
        
    def _mktest(self):
        d = os.path.join(self.basedir, "test")
        if not os.path.exists(d):
            os.mkdir(d)
        
if __name__ == "__main__":
    unittest.main()
