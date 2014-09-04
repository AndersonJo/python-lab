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
    
    def test_president(self):
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

    def test_sum_double(self):
        """
        두개의 숫자가 주어지고, 둘의 합계를 리턴시키세요. 만약 둘의 숫자가 같다면 합의 곱하기 2를 해주세요
        """
        self.assertEqual(3, yourtest.sum_double(1, 2))
        self.assertEqual(5, yourtest.sum_double(3, 2))
        self.assertEqual(-1, yourtest.sum_double(-1, 0))
        self.assertEqual(12, yourtest.sum_double(3, 3))
        self.assertEqual(0, yourtest.sum_double(0, 0))
        self.assertEqual(1, yourtest.sum_double(0, 1))
        self.assertEqual(7, yourtest.sum_double(3, 4))
    
    def test_monkey_troble(self):
        """
        우리에게는 두 마리의 원숭이가 있으며, monkey_trouble 함수는 두마리의 원숭이가 웃는지 안웃는지 나타냅니다.
        만약 두마리 모두 웃거나, 안웃으면 괜찮지만, 하나는 웃고 하나는 안 웃으면 문제가 생깁니다.
        """
        self.assertEqual(True, yourtest.monkey_trouble(True, True))
        self.assertEqual(True, yourtest.monkey_trouble(False, False))
        self.assertEqual(False, yourtest.monkey_trouble(True, False))
        self.assertEqual(False, yourtest.monkey_trouble(False, True))
        
    def test_diff21(self):
        """
        주어진값과 21과의 절대값(absolute) 차이를 리턴시키세요.
        만약 그 차이값이 21을 넘을 경우, 그 차이값에 2를 곱하세요. 
        """
        self.assertEqual(2, yourtest.diff21(19))
        self.assertEqual(11, yourtest.diff21(10))
        self.assertEqual(0, yourtest.diff21(21))
        self.assertEqual(2, yourtest.diff21(22))
        self.assertEqual(8, yourtest.diff21(25))
        self.assertEqual(18, yourtest.diff21(30))
        self.assertEqual(21, yourtest.diff21(0))
        self.assertEqual(20, yourtest.diff21(1))
        self.assertEqual(19, yourtest.diff21(2))
        self.assertEqual(22, yourtest.diff21(-1))
        self.assertEqual(23, yourtest.diff21(-2))
        self.assertEqual(58, yourtest.diff21(50))
        
    def test_parrot_trouble(self):
        """
        우리는 아주 시끄러운 앵무새 한마리를 키우고 있다. 
        parrot_trouble함수는 두개의 parameters 를 받는다. 
        첫번째는 이 앵무새가 우는지 안우는지..
        두번째는 시간이다. (0~24 사이의 시간)
        
        만약 이 앵무새가 7시 이전 또는 20시 이후에 시끄럽게 울면 분명 이웃집에서 난리가 날것이다.
        문제가 생겼는지 안생겼는지 알아보는 함수를 만들어보자 
        """
        self.assertEqual(True, yourtest.parrot_trouble(True, 6))
        self.assertEqual(False, yourtest.parrot_trouble(True, 7))
        self.assertEqual(False, yourtest.parrot_trouble(False, 6))
        self.assertEqual(True, yourtest.parrot_trouble(True, 21))
        self.assertEqual(False, yourtest.parrot_trouble(False, 21))
        self.assertEqual(False, yourtest.parrot_trouble(False, 20))
        self.assertEqual(True, yourtest.parrot_trouble(True, 23))
        self.assertEqual(False, yourtest.parrot_trouble(False, 23))
        self.assertEqual(False, yourtest.parrot_trouble(True, 20))
        self.assertEqual(False, yourtest.parrot_trouble(False, 12))
        

        
if __name__ == "__main__":
    unittest.main()
