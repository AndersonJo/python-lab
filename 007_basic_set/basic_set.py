# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import yourtest
import unittest


class SetTest(unittest.TestCase):
    
    def setUp(self):
        self.programmers = set(['Chang Min', 'Byung Du', 'Jobs', 'Mike'])
        self.managers = set(['Chang Min', 'Kim Jin'])
        self.designers = set(['Alice', 'Mike', 'Jane', 'Marvin', 'Jake', 'Finn'])
        self.marketers = set(['Marvin', 'Jake', 'Chang Min'])
        self.args = [self.programmers, self.managers, self.designers, self.marketers]
    
    
    def test_basic_set(self):
        data = ['python', 'foo', 'foo', 'python', 'x-man']
        self.assertEqual(set(['python', 'foo', 'x-man']), yourtest.basic_set(data))
        
    def test_employees(self):
        """
        Returns a set of whole employees.
        """
        answer = set(['Mike', 'Jake', 'Jobs', 'Byung Du', 'Marvin', 'Kim Jin', 'Alice', 'Chang Min', 'Finn', 'Jane'])
        self.assertEqual(answer, yourtest.get_employees(*self.args))
        
    def test_engineering_management(self):
        """
        Returns the group of people working as both programmers and managers.
        """
        answer = set(['Chang Min'])
        your_answer = yourtest.get_engineering_management(*self.args)
        self.assertEqual(answer, your_answer)
    
    def test_fulltime_management(self):
        """
        who is the full time manager?
        """
        answer = set(['Kim Jin'])
        your_answer = yourtest.get_fulltime_management(*self.args)
        self.assertEqual(answer, your_answer)
    
    def test_add(self):
        """
        Add  the teacher Chang Min
        """
        data = set(['alice', 'mike', 'foo'])
        answer = set(['alice', 'mike', 'foo', 'Chang Min'])
        self.assertEqual(answer, yourtest.add_changmin(data))
    
    def test_remove(self):
        """
        Remove the foo member
        """
        data = set(['alice', 'mike', 'foo'])
        answer = set(['alice', 'mike'])
        self.assertEqual(answer, yourtest.remove_foo(data))
    
    def test_is_programmer_or_designer(self):
        self.assertEqual(True, yourtest.is_programmer_or_designer('Chang Min', self.programmers, self.designers))
        self.assertEqual(True, yourtest.is_programmer_or_designer('Jobs', self.programmers, self.designers))
        self.assertEqual(True, yourtest.is_programmer_or_designer('Alice', self.programmers, self.designers))
        self.assertEqual(True, yourtest.is_programmer_or_designer('Finn', self.programmers, self.designers))
        self.assertEqual(False, yourtest.is_programmer_or_designer('Professor X', self.programmers, self.designers))
        self.assertEqual(False, yourtest.is_programmer_or_designer('Jung Ah', self.programmers, self.designers))
        self.assertEqual(False, yourtest.is_programmer_or_designer('', self.programmers, self.designers))
    
    def test_subset(self):
        """
        Is the first argument is the subset of the second argument?
        """
        self.assertEqual(True, yourtest.superset(set(['a', 'b']), set(['a', 'b', 'c'])))
        self.assertEqual(True, yourtest.superset(set([1,2,3]), set([1,2,3,4,5])))
        self.assertEqual(False, yourtest.superset(set(['a', 'b']), set(['a'])))
        self.assertEqual(False, yourtest.superset(set([1,2,3]), set([1])))
        
    
        
        

if __name__ == "__main__":
    unittest.main()
