import re

# crawling_page="http://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=103&sid2=243&oid=021&aid=0002345652"
# article = BeautifulSoup(urlopen(crawling_page), "html.parser")
# object = article.find(id='articleBodyContents')

def remove_ssa(obj):
    object = obj
    for i in range(len(object.find_all("script"))):
        object.script.decompose()
    for i in range(len(object.find_all("span"))):
        object.span.decompose()
    for i in range(len(object.find_all("a"))):
        object.a.decompose()
    return object

def preprocessing(object, company):

    if company == "연합뉴스":
        remove_ssa(object)
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
        remove_ssa(object)
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

    elif company == "경향신문":
        remove_ssa(object)
        for i in range(len(object.find_all('b'))):
            object.b.decompose()
        for i in range(len(object.find_all('strong'))):
            object.strong.decompose()
        for i in range(len(object.find_all('div'))):
            object.div.decompose()
        text = object.get_text()
        text = re.split("▶ 경향신문 SNS", text)[0]
        text = re.split(r"<[가-힣]+ 기자 [A-Za-z0-9\._+]+@kyunghyang.com>", text)[0]
        text = re.split(r"<[가-힣\s]>", text)[0]
        text = text.strip()
        return text

    elif company == "오마이뉴스":
        remove_ssa(object)
        text = object.get_text()
        text = re.split(r"저작권자\(c\)", text)[0]
        text = re.split(r"[오마이뉴스 [가-힣\s]+]", text)[1]
        text = text.strip()
        return text

    elif company == "매일경제":
        remove_ssa(object)
        text = object.get_text()
        text = re.split(r"[[가-힣\s=]+기자]", text)[0]
        text = text.strip()
        return text

    elif company == "아시아경제":
        for i in range(len(object.find_all("script"))):
            object.script.decompose()
        for i in object.find_all("span","end_photo_org end_photo_align_left"):
            i.clear()
        for i in range(len(object.find_all("a"))):
            object.a.decompose()
        text = object.get_text()
        text = re.split(r"<ⓒ세계를 보는 창 경제를 보는 눈, 아시아경제 무단전재 배포금지>", text)[0]
        text = text.strip()
        return text

    elif company == "문화일보":
        remove_ssa(object)
        text = object.get_text()
        text = re.split(r"[가-힣]+ 기자 [A-Za-z0-9\._+]+@munhwa.com", text)[0]
        text = re.split(r"<종합문화팀>", text)[0]
        text = text.strip()
        return text

    elif company == "헤럴드경제":
        remove_ssa(object)
        text = object.get_text()
        text = re.split(r"[가-힣]+ 기자/[A-Za-z0-9\._+]+@heraldcorp.com", text)[0]
        text = text.strip()
        return text

    elif company == "뉴시스":
        remove_ssa(object)
        text = object.get_text()
        text = re.split(r"[가-힣]+ 기자 =", text)[1]
        text = re.split(r"[A-Za-z0-9\._+]+@newsis.com", text)[0]
        text = text.strip()
        return text

    elif company == "한국경제":
        remove_ssa(object)
        text = object.get_text()
        text = re.split(r"[[\s]+[가-힣]+ 기자[\s]+]", text)[1]
        text = re.split(r"[가-힣]+ 기자 [A-Za-z0-9\._+]+@hankyung.com", text)[0]
        text = text.strip()
        return text

    elif company == "국민일보":
        for i in range(len(object.find_all("script"))):
            object.script.decompose()
        for i in object.find_all("span","end_photo_org"):
            i.clear()
        for i in range(len(object.find_all("a"))):
            object.a.decompose()
        text = object.get_text()
        text = re.split(r"[가-힣]+ [가-힣]+ [A-Za-z0-9\._+]+@kmib.co.kr", text)[0]
        text = text.strip()
        return text

    elif company == "머니투데이":
        remove_ssa(object)
        text = object.get_text()
        text = re.split(r"[머니투데이 [가-힣\s]+]", text)[1]
        text = re.split(r"[가-힣]+ 기자 [A-Za-z0-9\._+]+@", text)[0]
        text = text.strip()
        return text

    elif company == "한겨례":
        remove_ssa(object)
        for i in range(len(object.find_all("b"))):
            object.b.decompose()
        text = object.get_text()
        text = re.split(r"\[한겨레\]", text)[1]
        text = re.split(r"[가-힣]+ 기자 [A-Za-z0-9\._+]+@hani.co.kr", text)[0]
        text = text.strip()
        return text

    elif company == "한국일보":
        remove_ssa(object)
        for i in range(len(object.find_all("b"))):
            object.b.decompose()
        text = object.get_text()
        text = re.split(r"[가-힣]+ 기자 [A-Za-z0-9\._+]+@hankookilbo.com", text)[0]
        text = text.strip()
        return text

    elif company == "조선일보":
        remove_ssa(object)
        for i in range(len(object.find_all("b"))):
            object.b.decompose()
        text = object.get_text()
        text = re.split(r"[[가-힣\s]+기자 [A-Za-z0-9\._+]+@chosun.com]", text)[0]
        text = text.strip()
        return text

    elif company == "세계일보":
        remove_ssa(object)
        for i in range(len(object.find_all("b"))):
            object.b.decompose()
        text = object.get_text()
        text = re.split(r"[가-힣\s]+기자 [A-Za-z0-9\._+]+@segye.com", text)[0]
        text = text.strip()
        return text
'''                
    elif company == "":
        return text
    
    elif company == "":
        return text

    else:

    return ""
'''

