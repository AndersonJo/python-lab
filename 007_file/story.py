# -*- encoding:utf-8 -*-
"""
Counter 클래스를 사용해서 
stories 파일안에 들은 단어중 가장 많이 나온 순서대로 정렬을 하세요

Counter 클래스는 dict를 subclassing하는 클래스이며
most_common() 메소드를 사용해서 정렬을 할 수 있습니다. 

그렇게 정렬된 데이터를 pickle을 사용해서 answer 파일에 저장하세요.

"""

from collections import Counter
from pprint import pprint
import codecs



with codecs.open('20140207_Seoul.txt', 'r', encoding='EUC-KR') as readFile:
    print readFile.readline()
    with codecs.open('write.txt', 'w', encoding='UTF-8') as writeFile:
        for line in readFile:
            splittedText = line.split('|')
            sido = splittedText[2]
            gun = splittedText[4]
            writeFile.write(sido + '|' + gun + '|')
            