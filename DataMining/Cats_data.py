import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import csv

session = requests.session()
session.headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6'
}

with open('cats_datamining.csv','w', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(('Название выставки','Клуб','Дата'))

for i in range(1,78):
    try:
        URL = f'http://ru-pets.ru/index.php?m=6&to=1&c=2&page={i}'
        res = session.get(URL)
        html = res.text
        soup = BeautifulSoup(html, 'lxml')
        cats_exhibiton = soup.select('div.listitem')
        for card_cats in cats_exhibiton:
          name = card_cats.h2.text.strip().split('.')[2].strip()
          name_club = card_cats.find_all('span',{'class':'fwb cl-804000'})[1].text
          date_exh = card_cats.h2.text.strip().split('.')[0].strip()
          with open('cats_datamining.csv','a', encoding='utf-8') as outfile:
              writer = csv.writer(outfile)
              writer.writerow((name, name_club, date_exh))
        
    except HTTPError as ht:
        print(ht)
    except Exception as ex:
        print(ex)