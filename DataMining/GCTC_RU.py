import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


session = requests.session()
session.headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6'
}


for i in range(1,13):
    try:
        URL = f'https://www.gctc.ru/main.php?id=98.{i}'
        res = session.get(URL)
        res.raise_for_status()
        html = res.text
        soup = BeautifulSoup(html, 'lxml')
        res = []
        month = soup.select_one('div.ie_infoh')
        day = ''
        for ta in month:
            if ta.name == 'h1':
                day = str(ta.text[:2])
            if ta.name == 'div':
                if ta.text.strip()[:4].isdigit():
                    buff = [day, i, ta.text.strip()[:4]]
                    res.append(buff)
    except HTTPError as ht:
        print(ht)
    except Exception as ex:
        print(ex)