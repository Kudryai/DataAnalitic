import requests
import json
import os
from dotenv import load_dotenv, find_dotenv
import csv

load_dotenv(find_dotenv())
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

url = f"https://api.vk.com/method/database.getCities/"
params = {'access_token':ACCESS_TOKEN,
          'country_id':1,
          'q':'Томск',
          'sort':6,
          'count':1,
          'v':5.131}
res = requests.get(url, params=params)
res_city = res.json()
print(res_city)

url = f"https://api.vk.com/method/database.getUniversities/"
params1 = {'access_token':ACCESS_TOKEN,
          'country_id':1,
          'city_id':144,
          'v':5.131}
res = requests.get(url, params=params1)
res_univer = res.json()
print(res_univer)

if res_city.get('response',''):
    city = res_city['response']['items']
    univer = res_univer['response']['items']
    result = [{
            'id': bam['id'],
            'name': bam['title'],
            'universites': [{
                'id':uni['id'],
                'name':uni['title'],
                'faculties':[{
                    'name': facul['title']
                }for facul in requests.get('https://api.vk.com/method/database.getFaculties/', 
                                                       params={'access_token':ACCESS_TOKEN,
                                                               'university_id':uni['id'],
                                                               'v':5.131}).json()['response']['items']]
                } for uni in univer]
        } for bam in city]
    with open('UniverInfo.json','w') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)
else:
    pass