# -*- coding:utf-8 -*-
'''
파이썬/안드로이드/빅데이터 개발자 조창민입니다.
컨설팅/개발문의/강의 문의는 이메일로 부탁드립니다
http://mket.biz
a141890@gmail.com
'''
import re
import unittest
import yourtest



class RegexBasic(unittest.TestCase):
    
    def test_word(self):
        """
        영어 단어를 잡아내는 regex를 만들어라
        """
        self.assertNotEqual(None, yourtest.english_catch("hello"))
        self.assertNotEqual(None, yourtest.english_catch("kiwi"))
        self.assertNotEqual(None, yourtest.english_catch("AWESOME"))
        self.assertNotEqual(None, yourtest.english_catch("foo "))
        self.assertNotEqual(None, yourtest.english_catch("hell_"))
        self.assertNotEqual(None, yourtest.english_catch("#($&(# chang min"))
        self.assertEqual(None, yourtest.english_catch("1234"))
        self.assertEqual(None, yourtest.english_catch("!@$$%$"))
        self.assertEqual(None, yourtest.english_catch("   "))
        self.assertEqual(None, yourtest.english_catch(""))
        
    def test_numbers(self):
        """
        숫자를 잡아내는 regex를 만들어라
        """
        self.assertNotEqual(None, yourtest.number("1234"))
        self.assertNotEqual(None, yourtest.number("foo sunny 9 zero"))
        self.assertNotEqual(None, yourtest.number("!@#%%#%5!@#"))
        self.assertEqual(None, yourtest.number("!@#%%#%!@#"))
        self.assertEqual(None, yourtest.number("one two three"))
        self.assertEqual(None, yourtest.number(""))
        self.assertEqual(None, yourtest.number("   "))
    
    def test_abc(self):
        """
        :) <-- 잡아내자 
        """
        self.assertNotEqual(None, yourtest.smile("is there anyone? :)"))
        self.assertNotEqual(None, yourtest.smile("haha :) sorry about that."))
        self.assertNotEqual(None, yourtest.smile("hey :) why don't you just try it?"))
        self.assertEqual(None, yourtest.smile("that means 1: beat it! 2: get out of my way"))
        self.assertEqual(None, yourtest.smile("(foo, mket, python)"))
        self.assertEqual(None, yourtest.smile(""))
        self.assertEqual(None, yourtest.smile("  "))
        
    
    def test_color(self):
        """
        color 그리고 colour 단어를 찾는 것을 구현해라
        """
        self.assertNotEqual(None, yourtest.color('color'))
        self.assertNotEqual(None, yourtest.color('colour'))
        self.assertEqual(None, yourtest.color('colo'))
        self.assertEqual(None, yourtest.color('cololcolo'))
        self.assertEqual(None, yourtest.color(''))
        self.assertEqual(None, yourtest.color('olor'))
        self.assertEqual(None, yourtest.color('coloul'))
        self.assertNotEqual(None, yourtest.color('hello color'))
        self.assertNotEqual(None, yourtest.color('hello colour xx'))
        self.assertNotEqual(None, yourtest.color('collourcolorcolol'))
        self.assertNotEqual(None, yourtest.color('collolcocolcolourlcollour'))
        
    def test_fruits(self):
        """
        과일 이름으로 시작하는 문장을 잡아내라
        중간에 있는 것은 유효하지 않다.
        """
        self.assertEqual(True, yourtest.start_fruit(u'참외는 맛있오!'))
        self.assertEqual(True, yourtest.start_fruit(u'수박도 맛있오!'))
        self.assertEqual(True, yourtest.start_fruit(u'포도도 맛있는데.. 비싸 ㅠㅠ'))
        self.assertEqual(True, yourtest.start_fruit(u'딸기는.. 캐 맛 있 어!'))
        self.assertEqual(False, yourtest.start_fruit(u'그래서 딸기가 진리.'))
        self.assertEqual(False, yourtest.start_fruit(u'호주산 고기가 최고'))
        self.assertEqual(False, yourtest.start_fruit(u'제이크! 앤 핀! 어드벤쳐타임 재미있음'))
        self.assertEqual(False, yourtest.start_fruit(u'과일중에 맛있는건.. 참외, 수박, 포도!'))
        self.assertEqual(False, yourtest.start_fruit(u''))
    
    def test_winner(self):
        """
        winner 라는 글자를 잡아낸다. 단 winner!는 잡히지 말아야한다.
        """
        self.assertNotEqual(None, yourtest.winner('winner winner'))
        self.assertEqual(None, yourtest.winner('winner! win'))
        self.assertEqual(None, yourtest.winner('winnner winne winnener winner! winneer'))
        self.assertNotEqual(None, yourtest.winner('winner! win winn er winner win'))
        self.assertNotEqual(None, yourtest.winner('winn win! winnerr! winnerw!'))
        
    def test_naming(self):
        """
        숫자 +공백+ 문장 +공백+ 숫자 
        
        이런형식의 문장에서 "문장" 부분을 캐치해서 리턴시켜라
        """
        self.assertEqual(u"hello", yourtest.get_sentence_among_decimals(u"1234  hello 3431"))
        self.assertEqual(u"움막", yourtest.get_sentence_among_decimals(u"15788    움막 1111122482"))
        self.assertEqual(u"사랑합니다", yourtest.get_sentence_among_decimals(u"9  사랑합니다 1"))
        self.assertEqual(u"Life", yourtest.get_sentence_among_decimals(u"9  Life 1"))
        self.assertEqual(None, yourtest.get_sentence_among_decimals(u"9  123 1"))
        self.assertEqual(None, yourtest.get_sentence_among_decimals(u"91"))
        self.assertEqual(None, yourtest.get_sentence_among_decimals(u""))
        self.assertEqual(None, yourtest.get_sentence_among_decimals(u" word "))
        self.assertEqual(None, yourtest.get_sentence_among_decimals(u"word"))
        
    def test_duplicate(self):
        """
        문장속의 같은 단어가 중복되어 사용된다면.. 
        해당 단어를 리턴시키자
        
        단어는 숫자/영어/한글을 포함할수 있다.
        """
        self.assertEqual(u"1234", yourtest.get_duplicate(u"1234 1234"))
        self.assertEqual(u"foo", yourtest.get_duplicate(u"foo is very dirty one. because foo is dirty"))
        self.assertEqual(u"password", yourtest.get_duplicate(u"password is 1234. so is the password"))
        self.assertEqual(u"매트릭스", yourtest.get_duplicate(u"매트릭스 영화는 멋지다. 왜냐하면 매트릭스이기 때문이다"))
        self.assertEqual(u"123456789", yourtest.get_duplicate(u"12345678901234567890"))
        self.assertEqual(None, yourtest.get_duplicate(u"하나둘셋"))
        self.assertEqual(None, yourtest.get_duplicate(u""))
   
        
        
if __name__ == "__main__":
    unittest.main()
