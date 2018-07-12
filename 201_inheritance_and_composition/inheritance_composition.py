# -*- coding:utf-8 -*-


import yourtest
import unittest
import random


class InheritanceAndCompositionTest(unittest.TestCase):

    def test_make_human(self):
        """
        인간 클래스를 만들어라. 
        이름, 직업, 소득 instance attributes 가  constructor에 사용된다.
        """
        cm = yourtest.Person(name=u'창민', job=u'프로그래머', pay=1000)
        self.assertEqual(u'창민', cm.name)
        self.assertEqual(u'프로그래머', cm.job)
        self.assertEqual(1000, cm.pay)

    def test_give_raise(self):
        """
        월급을 percent 단위로 올려주는 함수를 만들어라
        """
        cm = yourtest.Person(name=u'창민', job=u'프로그래머', pay=1000)
        self.assertEqual(1300, cm.give_raise(0.3))
        self.assertEqual(1430, cm.give_raise(0.1))
        self.assertEqual(2145, cm.give_raise(0.5))
        self.assertEqual(2145, cm.give_raise(0))

    def test_manager(self):
        """
        창민 사원이 매니져로 승진하였다.
        __unicode__(self) 함수를 사용한다
        """
        cm = yourtest.Manager(u'창민', u'스크럼마스터', 1500)
        self.assertEqual(u"스크럼마스터 창민", unicode(cm))

    def test_manager2(self):
        """
        창민 스크럼마스터에게 월급 인상을 하려고 한다.
        사원과 다르게.. 매니져에게는 자동으로 보너스 0.1이 추가된다.
        """
        cm = yourtest.Manager(u'창민', u'스크럼마스터', 1500)
        self.assertEqual(2100, cm.give_raise(0.3))
        self.assertEqual(2520, cm.give_raise(0.1))
        self.assertEqual(4032, cm.give_raise(0.5))
        self.assertEqual(4435, cm.give_raise(0))
        self.assertEqual(6652, cm.give_raise(0, bonus=0.5))

    def test_composition(self):
        """
        부서를 만들고자 한다.
        """
        david = yourtest.Manager('David', u'프로그래머', 400)
        designer = yourtest.Manager(u'최사랑', u'디자이너', 400)
        salesman = yourtest.Manager(u'김달배', u'영업', 600)
        leader = yourtest.Manager(u'조창민', u'팀장', 800)
        department = yourtest.Department(david, designer, salesman, leader)

        self.assertEqual([david, designer, salesman, leader], department.persons)
        self.assertEqual(2200, department.get_total_pay())


if __name__ == "__main__":
    unittest.main()
