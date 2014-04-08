#-*- encoding:utf-8 -*-
import unittest
_ANSWERS = {
    ('Hiabc', 'abc'):True,
    ('AbC', 'HiaBc'): True,
    ('abc', 'abXabc'): True,
    ('Hiabc', 'abcd'): False,
    ('Hiabc', 'bc'): True,
    ('Hiabcx', 'bc'): False,
    ('abc', 'abc'): True,
    ('xyz', '12xyz'): True,
    ('yz', '12xz'): False,
    ('Z', '12xz'): True,
    ('12', '12'): True,
    ('abcXYZ', 'abcDEF'): False,
    ('ab', 'ab12'): False,
    ('ab', '12ab'): True,
}
      


class UnitTest(unittest.TestCase):
    
    def setUp(self):
        self.answers = _ANSWERS
        self.func = end_other
    
    def test_all(self):
        for args, answer in self.answers.items():
            returnValue = self.func(*args)
            errMsg = "\nArguments: %s %s \n답: %s \n당신의 답: %s"% (args[0], args[1], answer, returnValue) 
            self.assertEqual(answer, returnValue, msg=errMsg)


def end_other(a, b):
    """
    여기다가 코드를 쓰세요.
    @param a (str)
    @param b (str)  
    @return (boolean) : 서로의 스트링간에.. 동일하게 끝나면은 True, 아니면 False. 
                        *대소문자는 무시한다
    """
    pass


if __name__ =="__main__":
    print dir(end_other)
    print help(end_other)
    unittest.main()
    