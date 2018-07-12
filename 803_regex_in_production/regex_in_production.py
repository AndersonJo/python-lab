# -*- coding:utf-8 -*-

import codecs
from hashlib import md5
import unittest

import yourtest


class RegexBasic(unittest.TestCase):
    def test_abusive(self):
        """
        채팅프로그램을 만들려고 한다.
        카카오톡과는 다르게.. 모르는 사람과 채팅하는 프로그램이다.
        문제는 일명 중딩, 초딩들이 너무나 많은 욕설을 남발하고 다닌다.
        
        욕을 캐치해내는 regex를 만들자.
        
        개새, 씹새, 짭새 <-- 이것들을 캐치해낸다.
        """

        self.assertNotEqual(None, yourtest.catch_abusive_words(u"안녕 씹새야"))
        self.assertNotEqual(None, yourtest.catch_abusive_words(u"술먹는데 짭새가 오는겨~"))
        self.assertEqual(None, yourtest.catch_abusive_words(u"새나라의 어린이는~"))
        self.assertEqual(None, yourtest.catch_abusive_words(u"짭짤하네.. "))
        self.assertEqual(None, yourtest.catch_abusive_words(u"개씹짭"))
        self.assertEqual(None, yourtest.catch_abusive_words(u"hello"))
        self.assertEqual(None, yourtest.catch_abusive_words(u""))
        self.assertEqual(None, yourtest.catch_abusive_words(u"    "))

    def test_email(self):
        """
        간단하게 이메일 오류체크하는 함수를 만들어라
        """
        self.assertEqual(True, yourtest.is_email(u"a141890@gmail.com"))
        self.assertEqual(True, yourtest.is_email(u"webmaster@korea.co.kr"))
        self.assertEqual(True, yourtest.is_email(u"jochangmin@chang.org"))
        self.assertEqual(True, yourtest.is_email(u"보이스@naver.com"))
        self.assertEqual(False, yourtest.is_email(u"@udemy.com"))
        self.assertEqual(False, yourtest.is_email(u"myway@gmail."))
        self.assertEqual(False, yourtest.is_email(u"wrong@hanmail"))
        self.assertEqual(False, yourtest.is_email(u"whatever@"))
        self.assertEqual(False, yourtest.is_email(u"1234@"))
        self.assertEqual(False, yourtest.is_email(u" "))
        self.assertEqual(False, yourtest.is_email(u"@"))

    def test_title(self):
        """
        게시판 제목 데이터가 들어왔다. 
        깔끌하게 글자를 정돈하고 싶다.
        
        스페이스 여러개는 한개로 바꾸고, 양옆의 스페이스는 없어야 한다.
        """
        self.assertEqual(u"쇼생크탈출 !! 와!!", yourtest.clean_sentence(u"쇼생크탈출  !! 와!!"))
        self.assertEqual(u"어드벤쳐 타임!", yourtest.clean_sentence(u"  어드벤쳐  타임!"))
        self.assertEqual(u"hello everyone.", yourtest.clean_sentence(u"hello everyone.     "))
        self.assertEqual(u"", yourtest.clean_sentence(u"   "))
        self.assertEqual(u"피 곤 ... 하 다.... 흐 .. 아..",
                         yourtest.clean_sentence(u" 피   곤   ... 하 다....   흐 .. 아..  "))

    def test_mongodb(self):
        """
        MongoDB에서 키값으로 쓰이는 것은.. 
        영어 + 숫자 24글자 짜리 단어이다. 
        
        MongoDB키값이 맞는지 아닌지 검사하는 함수를 만들어라
        """
        self.assertEqual(True, yourtest.is_mongodb(u'53a47c1e1f78f01c1013955a'))
        self.assertEqual(True, yourtest.is_mongodb(u'53a47c261f78f01c33ed51a8'))
        self.assertEqual(False, yourtest.is_mongodb(u'__a47c561f78f01cd172681b'))
        self.assertEqual(False, yourtest.is_mongodb(u'13a47c561f78f01cd172681'))
        self.assertEqual(False, yourtest.is_mongodb(u'53a47c88!f78f01d826afdbb'))
        self.assertEqual(False, yourtest.is_mongodb(u'+3a47cabdf78f01d826afdbb'))
        self.assertEqual(False, yourtest.is_mongodb(u'6d47bf8'))
        self.assertEqual(False, yourtest.is_mongodb(u'   '))
        self.assertEqual(False, yourtest.is_mongodb(u''))

    def test_naver(self):
        """
        웹싸이트 주소가 내가 찾는 주소인지 맞는지 확인하는 함수를 만들어라
        
        http://naver.com 으로 시작하는 모든 주소
        
        문제는 .. 다음과 같은 주소이다.
        http://sports.news.naver.com
        
        앞에 서브 호스트 네임이 붙어 있다. 
        sports.news <= 요거
        
        이런것까지 모조리 잡아내야한다.
        """
        self.assertEqual(True, yourtest.naver(u'http://naver.com'))
        self.assertEqual(True, yourtest.naver(u'http://naver.com/sports/index.nhn?category=baseball'))
        self.assertEqual(True, yourtest.naver(u'http://shopping.naver.com/'))
        self.assertEqual(True, yourtest.naver(u'http://naver.com/sports/index.nhn?category=baseball'))
        self.assertEqual(True, yourtest.naver(
            u'http://news.naver.com/main/read.nhn?oid=055&sid1=103&aid=0000280477&mid=shm&mode=LSD&nh=20140620213340'))
        self.assertEqual(True, yourtest.naver(u'http://blog.naver.com/ani_changa/220036454221'))
        self.assertEqual(False, yourtest.naver(u'http://www.changkwang.kr/'))
        self.assertEqual(False, yourtest.naver(u'http://stackoverflow.com/'))
        self.assertEqual(False,
                         yourtest.naver(u'http://stackoverflow.com/questions/24333618/django-context-not-rendering'))

    def test_stackoverflow(self):
        """
        Stackoverflow의 내용을 가져오려고 한다.
        
        HTML 파일이 주어진다.
        
        여기서 Title을 꺼내보자
        
        Facebook Opengraph API의 방식을 이용한다.
        """
        correct_answer = "672b816b8a9eb1467a4ad6599718e8f4"
        your_answer = None
        with codecs.open('stackoverflow.html', 'rt', encoding='UTF-8') as f:
            your_answer = yourtest.stackoverflow(f.read())

        self.assertEqual(correct_answer, self.hashcode(your_answer))


    def test_phone(self):
        """
        핸드폰 번호를 찾아내라.
        한글로도 쓰여져 있을수 있다.
        
        1 - 일
        2 - 이
        3 - 삼
        4 - 사
        5 - 오
        6 - 육
        7 - 칠
        8 - 팔
        9 - 구
        0 - 공
        
        3글자 4글자 4글자 가 들어가는 것을 원칙으로 한다.
        예를 들어서
        010-1234-5678
        은 맞지만
        010-1234-56789 는 틀리다.
        
        앞자리는 010 (또는 일치하는 한글) 만 들어간다. 
        즉.. 016, 018 등등은 여기서 캐치하지 않는다.
        
        예제)
        
        공10-1234-5678
        공일공 1234-5678
        010-일이삼4 567팔
        
        re.findall 을 사용한다.
        리턴시 리스트로 리턴이 되어야한다.
        """
        phones = []
        with codecs.open('phone.txt', 'rt', encoding='UTF-8') as f:
            phones = yourtest.find_all_phones(f.read())

        correct_answer = '2894a918d791e4025bcccc5e53276e50'
        your_answer = self.hashcode(''.join(phones))
        self.assertEqual(correct_answer, your_answer)

    def hashcode(self, data):
        m = md5()
        m.update(data)
        return m.hexdigest()


if __name__ == "__main__":
    unittest.main()

