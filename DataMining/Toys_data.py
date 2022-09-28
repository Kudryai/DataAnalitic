import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import csv

session = requests.session()
session.headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6'
}

# Первый блок, сбор ссылок всех игрушек
urls_all_toys = []
for i in range(1,18):
    try:
        URL = f'https://tomsk.richfamily.ru/catalog/igrushki/myagkie/?PAGEN_1={i}'
        res = session.get(URL)
        html = res.text
        soup = BeautifulSoup(html, 'lxml')
        toy_urls = soup.find('div', {'class':'kkb_catalog-content-main'}).find_all('a',href=True)
        for url in toy_urls:
             if url['href'] != '/basket/':
                urls_all_toys.append(url['href'])
    except HTTPError as ht:
        print(ht)
    except Exception as ex:
        print(ex)

# Второй блок сбора информации
with open('toys_datamining.csv','w', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(('Имя','Цена','Длинна','Высота','Ширина'))

    
for j in range(len(urls_all_toys)):
    try:
        URL = f'https://tomsk.richfamily.ru{urls_all_toys[j]}'
        res = session.get(URL)
        html = res.text
        soup = BeautifulSoup(html, 'lxml')
        toy_name = soup.select_one('h1').text
        toy_price = soup.select_one('div.kkb_order-block__add-discount').text.split('\t')
        length = soup.select_one('span.prop_code_DLINA_SM').text
        height = soup.select_one('span.prop_code_VYSOTA_SM').text
        width = soup.select_one('span.prop_code_SHIRINA_SM').text
        with open('toys_datamining.csv','a', encoding='utf-8') as outfile:
          writer = csv.writer(outfile)
          writer.writerow((toy_name,toy_price[1].strip(), length, height, width))
        
    except HTTPError as ht:
        print(ht)
    except Exception as ex:
        with open('toys_datamining.csv','a', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow((toy_name,toy_price[1].strip(),0,0,0))