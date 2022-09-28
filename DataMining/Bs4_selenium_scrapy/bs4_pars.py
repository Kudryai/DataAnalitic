import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


URL = 'http://books.toscrape.com/'
session = requests.session()
session.headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6'
}

try:
    res = session.get(URL)
    res.raise_for_status()
    html = res.text
    soup = BeautifulSoup(html, 'lxml')

    ol = soup.select_one('ol.row')
    lis = ol.select('li')
    for li in lis:   
        name_obj = li.select_one('h3 a')
        if name_obj:
            name = name_obj['title']
        else:
            name = ''
        raiting = li.select_one('p.star-rating')
        raiting = raiting['class'][1]
        price_obj = li.select_one('div.product_price p')
        if price_obj:
            price = price_obj.text.split('£')[1]
        else:
            price = ''

        book_info = {
            'name': name,
            'rating': raiting,
            'price': price
        }
        print(book_info)

except HTTPError as ht:
    print(ht)
except Exception as ex:
    print(ex)