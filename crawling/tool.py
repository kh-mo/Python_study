import re

# crawling_page="http://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=103&sid2=243&oid=020&aid=0003133066"
# article = BeautifulSoup(urlopen(crawling_page), "html.parser")
# object = article.find(id='articleBodyContents')
# company = "동아일보"

def preprocessing(object, company):

    if company == "연합뉴스":
        for i in range(len(object.find_all("script"))):
            object.script.decompose()
        for i in range(len(object.find_all("span"))):
            object.span.decompose()
        for i in range(len(object.find_all("a"))):
            object.a.decompose()
        # for i in range(len(object.find_all("br"))):
        #     object.br.decompose()
        text = object.get_text()
        if "photo@yna.co.kr" in text:
            text = re.split(r"photo@yna.co.kr", text.split("=연합뉴스) ")[1])[0]
        elif "기자 = " in text:
            text = re.split(r"[A-Za-z0-9\._+]+@yna.co.kr", text.split("기자 = ")[1])[0]
        else:
            text = text.strip()
        return text

    elif company == "동아일보":
        for i in range(len(object.find_all("script"))):
            object.script.decompose()
        for i in range(len(object.find_all("span"))):
            object.span.decompose()
        for i in range(len(object.find_all("a"))):
            object.a.decompose()
        text = object.get_text()
        if "[동아일보]" in text:
            text = text.split("[동아일보]")[1]
            text = re.split(r"[가-힣]+ 기자 [A-Za-z0-9\._+]+@donga.com", text)[0]
            text = text.split("/ ⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지")[0]
        elif "[동아닷컴]" in text:
            text = text.split("[동아닷컴]")[1]
            text = re.split(r"[가-힣]+ 동아닷컴 기자 [A-Za-z0-9\._+]+@donga.com", text)[0]
            text = text.split("/ ⓒ 동아일보 & donga.com, 무단 전재 및 재배포 금지")[0]
        else:
            text = text.strip()
        return text
'''

    elif company == "":
    elif company == "":
    elif company == "":
    elif company == "":
    elif company == "":
    elif company == "":
    else:

    return ""
'''