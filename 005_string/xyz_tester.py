#-*- encoding:utf-8 -*-
import re
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
        print "*********** Unittest Start ************".center(70)
    
    def test_all(self):
        for q, a in self.answers.items():
            returnValue = self.func(q)
            errMsg = u"틀렵습니다 %-20s Yours: %-10s Correct Answer: %s"% (q, returnValue, a)
            try:
                self.assertEqual(a, returnValue, msg=errMsg)
            except AssertionError as e:
                print e


def xyz_finder(s):
    """
    여기다가 코드를 쓰세요.
    @return (boolean) : 'xyz'가 있으면 True를 리턴시킵니다. 단 ".xyz"는 인정되지 않습니다.
    """
    pass

if __name__ =="__main__":
    unittest.main()