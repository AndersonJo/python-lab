#-*- encoding:utf-8 -*-
import unittest

_ANSWERS = {
    'abcxyz': True,
    'abc.xyz': False,
    'xyz.abc': True,
    'abcxy': False,
    'xyz': True,
    'xy': False,
    'x': False,
    '': False,
    'abc.xyzxyz': True,
    '.xyz': False,
    '12.xyz': False,
    '12xyz': True,
    '1.xyz.xyz2.xyz': False,   
}

class XYZUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.answers = _ANSWERS
        self.func = xyz_finder
    
    def test_all(self):
        for q, a in self.answers.items():
            returnValue = self.func(q)
            errMsg = "\n"+  q + u" => 정답:" + unicode(a) + u"\n 당신이 내준 값:"+ unicode(returnValue) + u"\n 틀려부렀어.. ㅜㅜ"
            self.assertEqual(a, returnValue, msg=errMsg)


def xyz_finder(s):
    """
    여기다가 코드를 쓰세요.
    @return (boolean) : 'xyz'가 있으면 True를 리턴시킵니다. 단 ".xyz"는 인정되지 않습니다.
    """
    pass

if __name__ =="__main__":
    unittest.main()