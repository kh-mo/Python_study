'''
- 페이지를 찾을 수 없거나, URL 해석에서 에러가 생긴 경우 HTTPError 발생
- 서버를 찾을 수 없는 경우 HTTPError 발생
- BeautifulSoup는 태그가 없으면 None 객체를 반환하고 None 객체 속 태그에 접근하면 AttributeError 발생
'''

from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

'''
<h1>An Interesting Title</h1>
'''