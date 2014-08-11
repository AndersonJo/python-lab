# HBI기술연구소 파이썬 강좌 - 조창민 #

안녕하세요

현재 HBI연구소에서 파이썬, Django, Collective Intelligence, Data Mining 을 가르치고 있는 조창민입니다.

해당 Repository는 파이썬 강의를 위해서 고안된 문제집입니다.

Documentation은 계속 업데이트 예정입니다.


### 개발자 조창민 ###

언제든지 연락 환영입니다. :)

이메일 : [a141890@gmail.com](a141890@gmail.com)

HBI연구소 : http://hbiedu.co.kr/curriculum/regular_detail.jsp?seq=781&flag=1


### 강의 내용 ###

프로그래밍은 태어나서 한번도 보지 못한 분들을 위해서 강좌를 개설하였습니다.

실무에서 사용되는 내용들로만 구성이 되어 있으며, 단기간안에 많은 분량을 나갑니다.

다음의 룰은 절대적으로 지켜져야 합니다.

* 지각하지 않습니다. (수업시작하자 중요한 내용 바로 나갑니다. 늦으면 나중에 못 따라옵니다.)
* 힘들어도 무조건 나옵니다. (한번 빠지면 그 다음 수업 절대로 듣지 못합니다.)

강의는 프로그래밍의 첫 단추인 "Hello world" 부터 나가지만, 시간이 지날수록 매우 심도있게 들어갑니다.

단순히 파이썬 언어를 배우는것을 넘어서 Django, Image Processing, Crawler, Data Mining, Collective Intelligence등의 라이브러리및 기술들을 연마합니다.

당연히 힘듭니다. 여러분들을 피터지게 연마시킬겁니다. 

하지만 끝까지 참고 이기시는분은 분명 다른 곳에서는 절대 배울수 없는 진짜 실무위주의 내용들을 배우게 됩니다.

화이팅 :) 인내, 겸손, 열정으로 배워봅시다!


# 경 고 #

아래의 내용은 강의 내용의 극히 일부분에 불과합니다. 혹시나 인터넷에서만 보고 강의 내용을 판단하지 말아주시기 바랍니다. 

아래의 내용은 강의 내용의 극히 일부분에 불과합니다. 혹시나 인터넷에서만 보고 강의 내용을 판단하지 말아주시기 바랍니다. 

아래의 내용은 강의 내용의 극히 일부분에 불과합니다. 혹시나 인터넷에서만 보고 강의 내용을 판단하지 말아주시기 바랍니다. 


# Level 1 - Linux Ubuntu #

제가 고등학교때 처음으로 리눅스를 배웠는데요. 당시에는 CentOS가 한참 서버용으로서 인기가 있었던 시절입니다.

요즘에는 CentOS보다는 Ubuntu가 대세인듯 하네요.

관리자 측면에서보다 개발자 측면에서보면 라이브러리들이 업데이트가 잘되서 개발이 편합니다.

```
#!bash

ls # 디렉토리 이동 
mkdir # 디렉토리 생성
pwd # 현재 위치
gedit 파일명 # gedit 실행
vi 파일명 # vi 실행
sudo 명령어 # root 권한으로 명령어 실행 
apt-get install 패키지 이름 # 패키지 설치
```


# Level 2 - Python Basic #

파이썬 철학
```
#!python

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
.
.
Namespaces are one honking great idea -- let's do more of those!
```



콘솔에서 간단한 연산 가능
```
#!python

a141890:~>python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 1 + 1
2
>>> 10/4
2
>>> 15%7
1
>>> 3**2
9
>>> 3**4
81
```

간단한 스트링 조작

```
#!python
>>> s = 'Hello Wolrd'

>>> print s
Hello Wolrd

>>> s.upper()
'HELLO WOLRD'

>>> s[:5]
'Hello'

```

Variable 그리고 Assignment...

다른 언어와 다르게 파이썬에는 Variable Declaration 또는 Initialization 이 없습니다.
```
#!python

>>> number = 13 # Assignment
>>> other = 20 # Assignment
>>> number + other
33
```

# Level 3 - Package, Module 그리고 Import#
* package : 디렉토리에 해당한다. 단! __init__.py가 있으며 __init__.py 가 해당 디렉토리라고 봐도 된다. 또한 해당 package의 내용을 읽기전 가장 먼저 __init__.py가 읽어진다.
* module : .py 로 끝나는 파이썬 파일이다. 강의시간에 모듈을 만들라고 하면 .py 확장자로 끝나는 파일을 만들라는 소리다.
* import 가져올것 # 패키지, 모듈, 또는 Attributes등을 가져온다. 
* from 어디어디 import 무엇 # 이런 형식으로도 가져올수 있다. 
* from 어디어디 import 무엇 as 새로운 변수 이름 # '무엇'을 새로운 변수 이름으로 받는다. 

예제 

```
#!python

a141890:temp>mkdir foo
a141890:temp>cd foo
a141890:foo>echo > __init__.py
a141890:foo>ls
__init__.py

a141890:foo>echo "NAME = 'Chang Min'" > chang.py
a141890:foo>cat chang.py
NAME = 'Chang'

a141890:foo>cd ..
a141890:temp>python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from foo import chang
>>> print chang.NAME
Chang Min
```