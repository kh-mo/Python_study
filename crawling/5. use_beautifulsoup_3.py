'''
children(자식)과 descendants(자손)의 개념
한 단계 아래 : children
n 단계 아래 : descendants
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)

for child in bsObj.find("table",{"id":"giftList"}).descendants:
    print(child)

for child in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(child)

    
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())