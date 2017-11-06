'''
정규표현식 연습 홈페이지 : https://www.regexpal.com/

이메일 예시 : abcd@naver.com
[a-zA-Z0-9]+@[a-zA-Z]+/.(com|net|org)

[a-zA-Z0-9]+ : []안의 어떠한 글자라도 들어갈 수 있으며 +는 몇 개가 되든 상관하지 않겠다는 의미
@ : 이메일에 딱 한개만 들어가야 하는 @
/. : 도메인 이후 있는 마침표 한 개
(com|net|org) : 마침표 이후 들어갈 수 있는 도메인 마침 표시

기타
* : *앞에 있는 글자를 0번 이상 나타냅니다
+ : +아에 있는 문자를 1번 이상 나타냅니다
[] : 대괄호 안에 있는 문자 중 하나가 나타납니다
() : 그룹으로 묶인 하위 표현식
{m,n} : {}앞에 있는 문자가 m번 이상, n번 이하 나타납니다
[^] : 대괄호 안에 있는 문자를 제외한 문자가 나타납니다
| : 분리할 때 사용하는 문자(원화표시와 함께 있는 문자, 알파벳 l(엘), I(아이)가 아님)
. : 문자 하나를 나타냅니다
^ : ^뒤의 글자가 문자열의 맨 앞에 나타납니다
\ : 특수 문자를 원래 의미대로 쓰게 하는 이스케이프 문자
$ : 문자열의 마지막을 나타내는 문자
?! : ?!뒤 문자는 포함하지 않는다
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")  ## BeautifulSoup(html, "lxml") 도 사용 가능(저수준)
images = bsObj.findAll("img", {"src":re.compile("\.\./img/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])