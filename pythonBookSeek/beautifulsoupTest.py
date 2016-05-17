from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTittle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None;
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except ArithmeticError as e:
        return None
    return title

title = getTittle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("title not found")
else:
    print(title)