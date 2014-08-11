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