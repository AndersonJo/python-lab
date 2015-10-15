# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://andersonjo.github.io/
a141890@gmail.com
'''

import yourtest
import unittest


class BasicStringTest(unittest.TestCase):
    """
    기본적인 스트링 사용법을 배웁니다
    """
    
    def test_hello_name(self):
        """
        인사를 하는 함수를 만들어보자. 
        예를 들어서 Bob 이라는 글자를 받으면 Hello Bob! 이 리턴되게 해야한다.
        """
        self.assertEqual('Hello Bob!', yourtest.hello_name('Bob'))
        self.assertEqual('Hello Alice!', yourtest.hello_name('Alice'))
        self.assertEqual('Hello X!', yourtest.hello_name('X'))
        self.assertEqual('Hello Dolly!', yourtest.hello_name('Dolly'))
        self.assertEqual('Hello Alpha!', yourtest.hello_name('Alpha'))
        self.assertEqual('Hello Omega!', yourtest.hello_name('Omega'))
        self.assertEqual('Hello Goodbye!', yourtest.hello_name('Goodbye'))
        self.assertEqual('Hello ho ho ho!', yourtest.hello_name('ho ho ho'))
        self.assertEqual('Hello xyz!!', yourtest.hello_name('xyz!'))
        self.assertEqual('Hello Hello!', yourtest.hello_name('Hello'))
    
    def test_length(self):
        """
        주어진 스트링의 글자 갯수를 세는 함수를 만들자
        (스페이스까지 글자로 포함한다)
        """
        self.assertEqual(5, yourtest.str_length('Hello'))
        self.assertEqual(0, yourtest.str_length(''))
        self.assertEqual(4, yourtest.str_length('1234'))
        self.assertEqual(1, yourtest.str_length('5'))
        self.assertEqual(11, yourtest.str_length('hh oo ww ss'))
        self.assertEqual(4, yourtest.str_length('    '))
    
    def test_length2(self):
        """
        주어진 스트링의 글자 갯수를 세는 함수를 만들자
        (스페이스는 포함하지 않는다)
        """
        self.assertEqual(5, yourtest.str_length2('Hello'))
        self.assertEqual(0, yourtest.str_length2(''))
        self.assertEqual(4, yourtest.str_length2('1234'))
        self.assertEqual(1, yourtest.str_length2('5'))
        self.assertEqual(8, yourtest.str_length2('hh oo ww ss'))
        self.assertEqual(0, yourtest.str_length2('    '))    
    
    
    def test_make_tags(self):
        """
        HTML TAG를 만들어 내는 함수를 만들어보자. 
        두개의 parameters를 받는다. 하나는 태그 이름, 다른 하나는 내용물이다.
        예를 들어서 make_tags('i', 'Hello') 라면..
        <i>Hello</i> 
        가 리턴되어야 한다.
        """
        self.assertEqual('<i>Yay</i>', yourtest.make_tags('i', 'Yay'))
        self.assertEqual('<i>Hello</i>', yourtest.make_tags('i', 'Hello'))
        self.assertEqual('<cite>Yay</cite>', yourtest.make_tags('cite', 'Yay'))
        self.assertEqual('<address>here</address>', yourtest.make_tags('address', 'here'))
        self.assertEqual('<body>Heart</body>', yourtest.make_tags('body', 'Heart'))
        self.assertEqual('<i>i</i>', yourtest.make_tags('i', 'i'))
        self.assertEqual('<i></i>', yourtest.make_tags('i', ''))
    
    
    def test_string_count(self):
        """
        두개의 스트링을 받는다. 
        첫번재 Text에서 두번째 글자가 몇번 나오는지 계산하는 함수를 만들자
        """
        self.assertEqual(4, yourtest.string_count('hello my name is name', ' '))
        self.assertEqual(2, yourtest.string_count('hello my name is name', 'name'))
        self.assertEqual(6, yourtest.string_count('abcdabdeabef abewfababe', 'ab'))
        self.assertEqual(1, yourtest.string_count('abcdabdeabef abewfababe', ' ab'))
        self.assertEqual(4, yourtest.string_count('good is always good! but good sometimes is not good', 'good'))
        self.assertEqual(0, yourtest.string_count('', 'hello'))
    
    def test_endswith(self):
        """
        두개의 스트링을 받는다.
        첫번째 Text가 두번째 글자로 끝나는지 유무를 판단하는 함수를 만들자
        """
        self.assertEqual(True, yourtest.string_endswith('Bob hello', 'hello'))
        self.assertEqual(False, yourtest.string_endswith('Bob hello!', 'hello'))
        self.assertEqual(True, yourtest.string_endswith('hi', 'hi'))
        self.assertEqual(False, yourtest.string_endswith('', 'bye'))
        self.assertEqual(False, yourtest.string_endswith('james where you at?', 'james'))
        self.assertEqual(False, yourtest.string_endswith('the day before the day is another day!', 'day'))
        self.assertEqual(True, yourtest.string_endswith('asdfqwerasdf', 'asdf'))
        self.assertEqual(True, yourtest.string_endswith('1234', '34'))
    
    def test_reverse(self):
        """
        주어진 글자를 거꾸로 만드는 함수를 만들자.
        """
        self.assertEqual('4321', yourtest.string_reverse('1234'))
        self.assertEqual('olleh boB', yourtest.string_reverse('Bob hello'))
        self.assertEqual("!aedi doog s'tahT", yourtest.string_reverse("That's good idea!"))
        self.assertEqual('', yourtest.string_reverse(''))
        self.assertEqual("   d    c   b  a", yourtest.string_reverse('a  b   c    d   '))
        
    
    def test_isdigit(self):
        """
        주어진 글자가(str) 숫자인지 알아보는 함수를 만들자 
        """
        self.assertEqual(True, yourtest.string_isdigit('1234'))
        self.assertEqual(False, yourtest.string_isdigit(''))
        self.assertEqual(False, yourtest.string_isdigit('1234!'))
        self.assertEqual(False, yourtest.string_isdigit('hello 1234'))
        self.assertEqual(True, yourtest.string_isdigit('0'))
    
    def test_split(self):
        """
        스페이스가 나올때마다 단어를 잘라서 list로 리턴시키는 함수를 만들자.
        예) "hello Chang Min Jo" --> ['hello', 'Chang', 'Min', 'Jo']
        """
        self.assertEqual(['hello', 'hi'], yourtest.string_split('hello hi'))
        self.assertEqual(['amuse', 'danddy', 'cool'], yourtest.string_split('amuse danddy cool'))
        self.assertEqual(['hi'], yourtest.string_split('hi'))
        self.assertEqual(['1', '2', '3', '4', '5'], yourtest.string_split('1 2 3 4 5'))
        self.assertEqual([''], yourtest.string_split(''))
        
    def test_strip(self):
        """
        주어진 문장의 양쪽의 스페이스를 없애는 함수를 만들자
        예) " space-x   is awesome     ' --> 'space-x   is awesome'
        """
        self.assertEqual('1 2 3 4 5', yourtest.string_strip(' 1 2 3 4 5 '))
        self.assertEqual('hello', yourtest.string_strip(' hello     '))
        self.assertEqual('', yourtest.string_strip('      '))
        self.assertEqual('x    y   x', yourtest.string_strip('     x    y   x '))
        self.assertEqual('apple', yourtest.string_strip('     apple'))
        self.assertEqual('banana', yourtest.string_strip('banana                 '))
        
    def test_upper(self):
        """
        주어진 문장의 단어를 모두 대문자로 만드는 함수를 만들자
        """
        self.assertEqual('BANANA', yourtest.string_upper('banana'))
        self.assertEqual('   APPLE', yourtest.string_upper('   appLE'))
        self.assertEqual('X-MINUS', yourtest.string_upper('X-MINUS'))
        self.assertEqual('1234', yourtest.string_upper('1234'))
        self.assertEqual('1234 PYTHON IS VERY SIMPLE', yourtest.string_upper('1234 python is very simple'))
        self.assertEqual('  MKET IS YOUR FRIEND  ', yourtest.string_upper('  mket IS your friEND  '))
    

        
if __name__ == "__main__":
    unittest.main()
