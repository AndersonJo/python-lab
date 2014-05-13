# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''

import yourtest
import unittest
import random


class DictionaryTest(unittest.TestCase):
    
    def test_gt12(self):
        """
        숫자 12s보다 크다면 True, 작거나 같다면 False
        """
        self.assertEqual(True, yourtest.gt12(13))
        self.assertEqual(False, yourtest.gt12(12))
        self.assertEqual(False, yourtest.gt12(0))
        self.assertEqual(False, yourtest.gt12(-4))
        self.assertEqual(True, yourtest.gt12(150))
    
    def atest_president(self):
        """
        당신은 박근혜 대통령의 경호실장이다.
        어떠한 위협으로부터도 지켜야 할 의무가 있다.
        최고 위험도 6부터 안전 1까지의 값을 리턴시켜라.
        
        위험
        6 = 이슬람 무장단체
        5 = 좀비
        4 = 친북단체
        
        안전
        3 = 평화주의자
        2 = 시민
        1 = 프로그래머
        
        그외
        0 
        """
        self.assertEqual(6, yourtest.president_safe(u"이슬람 무장단체"))
        self.assertEqual(5, yourtest.president_safe(u"좀비"))
        self.assertEqual(4, yourtest.president_safe(u"친북단체"))
        self.assertEqual(3, yourtest.president_safe(u"평화주의자"))
        self.assertEqual(2, yourtest.president_safe(u"시민"))
        self.assertEqual(1, yourtest.president_safe(u"프로그래머"))
        self.assertEqual(0, yourtest.president_safe(u"오바마"))
    
    def test_drama(self):
        """
        드라마 촬영중이다.
        카메라, 음향, 조명 모두 만족한다면 True를 리턴시켜라
        단 just_go 싸인이 떨어지면 무조건 True를 리턴시켜라.
        """
        self.assertEqual(True, yourtest.is_ok(camera=True, music=True, lighting=True))
        self.assertEqual(False, yourtest.is_ok(camera=True, music=True, lighting=False))
        self.assertEqual(False, yourtest.is_ok(camera=True, lighting=False))
        self.assertEqual(False, yourtest.is_ok(lighting=False))
        self.assertEqual(False, yourtest.is_ok())
        self.assertEqual(True, yourtest.is_ok(just_go=True))
        self.assertEqual(True, yourtest.is_ok(camera=True, just_go=True))
    
    def test_church(self):
        """
        교회가는 날이다.
        만약 일요일이면 무조건 나가야한다.
        하지만 금요예배는 되도록이면 참여하고자 한다.
        일이 없다면 금요예배는 참여가 가능하다.
        그외에는 안간다.
        """    
        self.assertEqual(True, yourtest.church(day='sunday'))
        self.assertEqual(True, yourtest.church(work=True, day='sunday'))
        self.assertEqual(True, yourtest.church(work=False, day='sunday'))
        self.assertEqual(False, yourtest.church())
        self.assertEqual(True, yourtest.church(day='friday'))
        self.assertEqual(True, yourtest.church(day='friday', work=False))
        self.assertEqual(False, yourtest.church(day='friday', work=True))
        self.assertEqual(False, yourtest.church(day='monday', work=False))
        self.assertEqual(False, yourtest.church(day='', work=False))
    
    def test_economy_risk(self):
        """
        환율이 1000원 이하  또는 1200이상이면 위험하다.
        하지만 경기붐을 탄다면 환율따위는 상관없다.
        위험신호를 체크하는 함수를 만들어라.
        """
        self.assertEqual(False, yourtest.economy_risk(rate=1100))
        self.assertEqual(True, yourtest.economy_risk(rate=1200))
        self.assertEqual(True, yourtest.economy_risk(rate=1000))
        self.assertEqual(True, yourtest.economy_risk(rate=0))
        self.assertEqual(True, yourtest.economy_risk(rate=-500))
        self.assertEqual(False, yourtest.economy_risk(rate=1000, boom=True))
        self.assertEqual(False, yourtest.economy_risk(rate=1500, boom=True))
        self.assertEqual(False, yourtest.economy_risk(rate=1200, boom=True))
        self.assertEqual(False, yourtest.economy_risk(rate=1100, boom=True))
        self.assertEqual(False, yourtest.economy_risk(rate=1100))
        
    def test_sum_without7(self):
        """
        모든 수를 합하세요. 
        단 7이 들어간 수는 피해주세요.
        """
        self.assertEqual(10, yourtest.sum_without7(1,2,3,4))
        self.assertEqual(0, yourtest.sum_without7(13487, 122, 88, -210))
        self.assertEqual(-1, yourtest.sum_without7(-1))
        self.assertEqual(0, yourtest.sum_without7(7))
        self.assertEqual(0, yourtest.sum_without7())
        self.assertEqual(0, yourtest.sum_without7(1270, 750, 64817, 777))
    
    

        
if __name__ == "__main__":
    unittest.main()
