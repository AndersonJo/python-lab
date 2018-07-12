# -*- coding:utf-8 -*-


import yourtest
import unittest


class StringTest(unittest.TestCase):
    
    def test_double_char(self):
        """
        주어진 스트링에서 모든 문자들을 두개로 만든 스트링을 리턴시키는 함수를 만들어라.
        """
        self.assertEqual('TThhee', yourtest.double_char('The'))
        self.assertEqual('AAAAbbbb', yourtest.double_char('AAbb'))
        self.assertEqual('HHii--TThheerree', yourtest.double_char('Hi-There'))
        self.assertEqual('WWoorrdd!!', yourtest.double_char('Word!'))
        self.assertEqual('!!!!', yourtest.double_char('!!'))
        self.assertEqual('', yourtest.double_char(''))
        self.assertEqual('aaaa', yourtest.double_char('aa'))
        
    def test_count_hi(self):
        """
        주어진 문장안에 hi 가 얼마나 많이 들어있는지 알아내는 함수를 만들어라.
        """
        self.assertEqual(1, yourtest.count_hi('abc hi ho'))
        self.assertEqual(2, yourtest.count_hi('ABChi hi'))
        self.assertEqual(2, yourtest.count_hi('hihi'))
        self.assertEqual(0, yourtest.count_hi(''))
        self.assertEqual(0, yourtest.count_hi('h'))
        self.assertEqual(1, yourtest.count_hi('hi'))
        self.assertEqual(0, yourtest.count_hi('Hi is no HI on ahI'))
        self.assertEqual(2, yourtest.count_hi('hiho not HOHIhi'))
        
    def test_cat_dog(self):
        """
        주어진 문장안에 cat 그리고 dog가 나온 횟수가 같으면 True 아니면 False
        를 리턴시키는 함수를 만들어라
        """
        self.assertEqual(True, yourtest.cat_dog('catdog'))
        self.assertEqual(False, yourtest.cat_dog('catcat'))
        self.assertEqual(True, yourtest.cat_dog('1cat1cadodog'))
        self.assertEqual(False, yourtest.cat_dog('catxxdogxxxdog'))
        self.assertEqual(True, yourtest.cat_dog('catxdogxdogxcat'))
        self.assertEqual(False, yourtest.cat_dog('catxdogxdogxca'))
        self.assertEqual(False, yourtest.cat_dog('dogdogcat'))
        self.assertEqual(True, yourtest.cat_dog('dogogcat'))
        self.assertEqual(False, yourtest.cat_dog('dog'))
        self.assertEqual(False, yourtest.cat_dog('cat'))
        self.assertEqual(True, yourtest.cat_dog('ca'))
        self.assertEqual(True, yourtest.cat_dog('c'))
        self.assertEqual(True, yourtest.cat_dog('d'))
        
    def test_end_other(self):
        """
        주어진 2개의 스트링중에, 둘중에 하나라도 같은 스트링으로 끝나면 True를 반환하는 함수를 만들어라.
        단! 대소문자는 상관하지 않는다.
        """
        self.assertEqual(True, yourtest.end_other('Hiabc', 'abc'))
        self.assertEqual(True, yourtest.end_other('AbC', 'HiaBc'))
        self.assertEqual(True, yourtest.end_other('abc', 'abXabc'))
        self.assertEqual(False, yourtest.end_other('Hiabc', 'abcd'))
        self.assertEqual(True, yourtest.end_other('Hiabc', 'bc'))
        self.assertEqual(False, yourtest.end_other('Hiabcx', 'bc'))
        self.assertEqual(True, yourtest.end_other('abc', 'abc'))
        self.assertEqual(True, yourtest.end_other('xyz', '12xyz'))
        self.assertEqual(False, yourtest.end_other('yz', '12xz'))
        self.assertEqual(True, yourtest.end_other('Z', '12xz'))
        self.assertEqual(True, yourtest.end_other('12', '12'))
        self.assertEqual(False, yourtest.end_other('abcXYZ', 'abcDEF'))
        self.assertEqual(False, yourtest.end_other('ab', 'ab12'))
        self.assertEqual(True, yourtest.end_other('ab', '12ab'))
        
    def test_xyz_there(self):
        """
        만약 xyz가 주어진 문장안에 있다면 True를 반환하는 함수를 만들어라. 
        단! .xyz는 인정되지 않는다. 
        """
        self.assertEqual(True, yourtest.xyz_there('abcxyz'))
        self.assertEqual(False, yourtest.xyz_there('abc.xyz'))
        self.assertEqual(True, yourtest.xyz_there('xyz.abc'))
        self.assertEqual(False, yourtest.xyz_there('abcxy'))
        self.assertEqual(True, yourtest.xyz_there('xyz'))
        self.assertEqual(False, yourtest.xyz_there('xy'))
        self.assertEqual(False, yourtest.xyz_there('x'))
        self.assertEqual(True, yourtest.xyz_there('abc.xyzxyz'))
        self.assertEqual(True, yourtest.xyz_there('abc.xxyz'))
        self.assertEqual(False, yourtest.xyz_there('.xyz'))
        self.assertEqual(False, yourtest.xyz_there('12.xyz'))
        self.assertEqual(True, yourtest.xyz_there('12xyz'))
        self.assertEqual(False, yourtest.xyz_there('1.xyz.xyz2.xyz'))
    
    def test_left2(self):
        """
        앞의 2글자를 뒤로 보내는 함수를 만들어라
        """
        self.assertEqual('lloHe', yourtest.left2('Hello'))
        self.assertEqual('vaja', yourtest.left2('java'))
        self.assertEqual('Hi', yourtest.left2('Hi'))
        self.assertEqual('deco', yourtest.left2('code'))
        self.assertEqual('tca', yourtest.left2('cat'))
        self.assertEqual('34512', yourtest.left2('12345'))
        self.assertEqual('ocolateCh', yourtest.left2('Chocolate'))
        self.assertEqual('icksbr', yourtest.left2('bricks'))
    
    def test_concate_short_long_short(self):
        """
        2개의 문장중을 길이를 잰다음
        short + long + short
        문장이 되도록 만드는 함수를 만든다.
        """
        self.assertEqual('hiHellohi', yourtest.concate_short_long_short('Hello', 'hi'))
        self.assertEqual('hiHellohi', yourtest.concate_short_long_short('hi', 'Hello'))
        self.assertEqual('baaab', yourtest.concate_short_long_short('aaa', 'b'))
        self.assertEqual('baaab', yourtest.concate_short_long_short('b', 'aaa'))
        self.assertEqual('bb', yourtest.concate_short_long_short('', 'bb'))
        self.assertEqual('aaa1234aaa', yourtest.concate_short_long_short('aaa', '1234'))
        self.assertEqual('bbaaabb', yourtest.concate_short_long_short('aaa', 'bb'))
        self.assertEqual('abba', yourtest.concate_short_long_short('a', 'bb'))
        self.assertEqual('abba', yourtest.concate_short_long_short('bb', 'a'))
        self.assertEqual('abxyzab', yourtest.concate_short_long_short('xyz', 'ab'))
        
    def test_without_end(self):
        """
        첫글자와 마지막글자를 제외한 스트링을 리턴시켜라
        """
        self.assertEqual('ell', yourtest.without_end('Hello'))
        self.assertEqual('av', yourtest.without_end('java'))
        self.assertEqual('ytho', yourtest.without_end('Python'))
        self.assertEqual('odin', yourtest.without_end('coding'))
        self.assertEqual('od', yourtest.without_end('code'))
        self.assertEqual('', yourtest.without_end('ab'))
        self.assertEqual('hocolate', yourtest.without_end('Chocolate!'))
        self.assertEqual('itte', yourtest.without_end('kitten'))
    
    def test_first_half(self):
        """
        주어진 문장의 절반에 해당하는 앞부분을 리턴시켜라
        """
        self.assertEqual('Woo', yourtest.first_half('WooHoo'))
        self.assertEqual('Hello', yourtest.first_half('HelloThere'))
        self.assertEqual('abc', yourtest.first_half('abcdef'))
        self.assertEqual('a', yourtest.first_half('ab'))
        self.assertEqual('', yourtest.first_half(''))
        self.assertEqual('01234', yourtest.first_half('0123456789'))
        self.assertEqual('kit', yourtest.first_half('kitten'))

    def test_cut(self):
        """
        5글자가 넘어가는 문장은 5글자로 잘라버리고 뒤에 "..." 을 붙이는 함수를 만든다.
        5글자 내외이면 그대로 출력한다.
        깔끔한 처리를 위해서 strip 함수가 필요할 것이다.
        """
        self.assertEqual('banan...', yourtest.cut5('banana'))
        self.assertEqual('apple', yourtest.cut5('apple'))
        self.assertEqual('abc', yourtest.cut5('abc'))
        self.assertEqual('d', yourtest.cut5('  d'))
        self.assertEqual('dayby...', yourtest.cut5('  daybyday '))
        self.assertEqual('my na...', yourtest.cut5('my name is Chang Min'))
        self.assertEqual('Life...', yourtest.cut5('Life is short, you need Python'))
        


if __name__ == "__main__":
    unittest.main()
