'''
- 동일한 정보를 다른 홈페이지에서 스크래핑 하는 방법- 

1. 모바일 버전 사용
2. 자바스크립트에서 필요한 정보 찾기
3. 정보가 url에 있을 수도 있음
4. 다른 소스로부터 온 정보
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

'''
- findAll(tagName, attributes)
tagName : tag 종류 (span, ....)
attributes : tag의 속성 (class, ...)

- get_text()
태그를 제거하고 텍스트만 남긴다
'''

nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
