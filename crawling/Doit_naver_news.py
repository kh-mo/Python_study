"""
제목(title)
날짜(date)
본문(body)
요약(sum_content)
신문사(company)

Assumption 1:
신문사별로 기사를 올리는 형태가 다르다
즉, 신문사별로 데이터를 수집해서 신문사에 맞게 전처리를 수행한다면
보다 깔끔한 데이터를 수집할 수 있을 것이다.
"""

import re
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen
from crawling.tool import preprocessing

# 날짜, 기준날짜, 페이지, 저장할 데이터프레임
dates = range(15)
base_time = datetime.datetime(2018, 3, 3)
pages = range(50)
result = pd.DataFrame({"title": [], "date": [], "body": [], "sum_content": [], "company": []})

# 크롤링할 날짜
for date in dates:
    dif_time = datetime.timedelta(days=date)
    present_time = (base_time - dif_time).strftime("%Y%m%d")
    print("날짜 :", present_time)
    pre_page_link = []
    # 크롤링할 페이지
    for page in pages:
        # 페이지 내 크롤링할 기사 리스트
        article_set_url = "http://news.naver.com/main/list.nhn?mode=LS2D&sid2=243&sid1=103&mid=shm&date="+present_time+"&page="+str(page+1)
        article_set = BeautifulSoup(urlopen(article_set_url), "html.parser")
        hrefs = article_set.find("div", {"class": "list_body newsflash_body"}).findAll("a")
        cur_page_link = list(set([link.attrs['href'] for link in article_set.find("div", {"class": "list_body newsflash_body"}).findAll("a")]))
        if cur_page_link == pre_page_link:
            print("break")
            break
        pre_page_link = cur_page_link[:]

        for crawling_page in cur_page_link:
            # 요약봇에서 summary 정보 수집
            sum_link = crawling_page.split('&')
            oid = [s for s in sum_link if "oid=" in s][0].replace("oid=", "")
            aid = [s for s in sum_link if "aid=" in s][0].replace("aid=", "")
            sum_link = "http://tts.news.naver.com/article/" + oid + "/" + aid + "/summary?callback=window.__jindo2_callback._2123"
            try:
                summary = BeautifulSoup(urlopen(sum_link), "html.parser")
            except (HTTPError, ConnectionResetError):
                break
            sum_content = summary.get_text()
            sum_content = sum_content.split("summary\":\"")[1].replace("\"});", "").replace(".",". ")

            # 요약정보가 없으면 break
            if '해당 기사는 요청하신 자동 요약문을 제공할 수 없습니다.' in sum_content:
                break

            try:
                article = BeautifulSoup(urlopen(crawling_page), "html.parser")
            except (AttributeError, IndexError, ConnectionResetError):
                break

            # 기사 제목 크롤링
            title = article.find(id='articleTitle').get_text()
            # 기사 신문사 크롤링
            company = article.find("div", {'class', 'press_logo'}).find('img').get('title')
            # 기사 본문 크롤링
            body = preprocessing(article.find(id='articleBodyContents'), company)

            d = {"title": [title], "date": [present_time], "body": [body], "sum_content": [sum_content], "company": [company]}
           result = result.append(pd.DataFrame(data=d))
        print("페이지 :", (page + 1))

result.to_csv("C:/Users/mo/Desktop/crawled_book.csv")
