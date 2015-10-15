# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://andersonjo.github.io/
a141890@gmail.com
'''

import yourtest
import unittest


class DictionaryTest(unittest.TestCase):
    
    def setUp(self):
        super(DictionaryTest, self).setUp()
    
    def test_basic(self):
        """
        그냥 동일한 dictionary를 리턴시키세요 
        """
        self.assertEqual({'name': 'Chang Min'}, yourtest.basic())
        
    def test_fast_search(self):
        """
        우리의 작은 영한사전에서, 한글뜻을 찾는 함수를 만드세요.
        만약 사전에 없는 단어라면 "살쪄" 를 리턴시키세요.
        """
        dictionary = {'banana': u'바나나',
                           'apple': u'사과',
                           'mket': u'앰켓',
                           'apocalypse': u'멸망', }
        
        self.assertEqual(u"앰켓", yourtest.fast_search(dictionary, 'mket'))
        self.assertEqual(u"바나나", yourtest.fast_search(dictionary, 'banana'))
        self.assertEqual(u"멸망", yourtest.fast_search(dictionary, 'apocalypse'))
        self.assertEqual(u"살쪄", yourtest.fast_search(dictionary, 'pizza'))
        
    def test_has_key(self):
        """
        이름과 나이를 수집해야합니다.
        문제는 아직 모든 데이터가 다 수집되지 않아서.. 
        이름이 없는 경우도 있습니다.
        
        데이터안에 이름이 있는지 없는지 알아내는 함수를 만드세요 
        """
        dictionary = {'mike': 13,
                      'alice': 24,
                      'shep': 30,
                      'bill': 22,
                      'steve': 51,}
        self.assertEqual(True, yourtest.has_name(dictionary, 'mike'))
        self.assertEqual(True, yourtest.has_name(dictionary, 'bill'))
        self.assertEqual(True, yourtest.has_name(dictionary, 'steve'))
        self.assertEqual(False, yourtest.has_name(dictionary, 'Chang Min'))
        self.assertEqual(False, yourtest.has_name(dictionary, ''))
        
    def test_add10(self):
        """
        학생들의 시험점수를 모두 매겼습니다.
        문제는 컴퓨터의 버그때문에 모든 학생의 점수가 10점씩 깍여있는 데이터가 출력됐습니다.
        교정하기 위해서는 모든 학생들의 점수를 10점씩 높여야 합니다.
        """
        scores = {'mike': {'english':80, 'math': 40, 'python': 10},
                 'alice': {'english':40, 'math': 10, 'python': 90},
                 'tony': {'english':65, 'math': 20, 'python': 45},
                 'andrew': {'english':0, 'math': 0, 'python': 30},}
        
        answer = {'mike': {'english':90, 'math': 50, 'python': 20},
                 'alice': {'english':50, 'math': 20, 'python': 100},
                 'tony': {'english':75, 'math': 30, 'python': 55},
                 'andrew': {'english':10, 'math': 10, 'python': 40},}
        self.assertEqual(answer, yourtest.add10(scores))
        
        
    def test_copy(self):
        """
        Shallow 카피를 하세요
        """
        chang = {'name': 'Chang Min', 'foods': ['pizza', 'icecream', 'fried chicken'], 'age': 19}
        result = yourtest.shallow_copy(chang)
        self.assertEqual(chang, result)
        result['foods'].append('burgerking')
        self.assertEqual(chang, result)
        chang['height'] = 183
        self.assertNotEqual(chang, result)
        
    
    def test_delete(self):
        """
        당신은 여러개의 창고를 갖고 있는 물류담당직원입니다.
        각각의 창고에는 여러과일들이 있습니다.
        
        문제는.. 창고안의 모든 banana가 벌레를 먹어서 버려야 합니다.
        데이터안의 banana를 모두 삭제시키세요
        (각각의 리스트안의 아이템들은 창고를 나타냅니다.)
        """
        stores = [
                  {'banana': 230, 'mango': 1023, 'melon': 32},
                  {'melon': 512, 'kiwi': 1000},
                  {'cherry': 40, 'banana': 500, 'grape': 1000, 'carrot': 700},
                  {'orange': 200, 'pepper': 10},
                  {},
                  ]
        
        answers = [
                  {'mango': 1023, 'melon': 32},
                  {'melon': 512, 'kiwi': 1000},
                  {'cherry': 40, 'grape': 1000, 'carrot': 700},
                  {'orange': 200, 'pepper': 10},
                  {},
                  ] 
        
        self.assertEqual(answers, yourtest.remove_banana(stores))
        
    def test_kwargs(self):
        """
        in 또는 not__in 을 구별하는 함수를 만들어라. 
        예를 들어서
        has_kwargs(apple__in=['apple', 'banana']) 
        에는.. apple이 주어진 리스트안에 존재하기 때문에 
        {'apple': True} 를 리턴시킨다.
        """
        self.assertEqual({'apple': True}, yourtest.has_kwargs(apple__in=['apple', 'banana']))
        self.assertEqual({'apple': False}, yourtest.has_kwargs(apple__not_in=['apple', 'banana']))
        self.assertEqual({'apple': False, 'banana':False}, yourtest.has_kwargs(apple__not_in=['apple', 'banana'], banana__in=['abc']))
        self.assertEqual({}, yourtest.has_kwargs())
        self.assertEqual({'monkey': False}, yourtest.has_kwargs(monkey__in=['shark', 'squid', 'fish']))
        
        
        
if __name__ == "__main__":
    unittest.main()
