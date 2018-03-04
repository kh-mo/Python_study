import re
# object = article.find(id='articleBodyContents')
def preprocessing(object, company):
    if company == "연합뉴스":
        for i in range(len(object.find_all("script"))):
            object.script.decompose()
        for i in range(len(object.find_all("span"))):
            object.span.decompose()
        for i in range(len(object.find_all("a"))):
            object.a.decompose()
        for i in range(len(object.find_all("br"))):
            object.br.decompose()
        text = object.get_text()
        if "photo@yna.co.kr" in text:
            text = re.split(r"photo@yna.co.kr", text.split("=연합뉴스) ")[1])[0]
        elif "기자 = " in text:
            text = re.split(r"[A-Za-z0-9\._+]+@yna.co.kr", text.split("기자 = ")[1])[0]
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
    elif company == "":
    else:

    return ""
'''