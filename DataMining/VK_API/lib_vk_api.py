import vk_api
import os
from dotenv import load_dotenv, find_dotenv
import csv

load_dotenv(find_dotenv())
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

vk_session = vk_api.VkApi(token=ACCESS_TOKEN)
vk = vk_session.get_api()

city = vk.database.getCities(country_id=1,q='Омск', count=1)
city_id = city['items'][0]['id'] if city ['count'] > 0 else None

if city_id:
    for word in ['цветы','флористика','магазин цветов']:
        groups = vk.groups.search(country_id=1, city_id=city_id, sort=6, q=word, count=500)
        groups_ids = [gr['id'] for gr in groups['items']]
        groups_info = vk.groups.getById(group_ids=groups_ids, fields=['contacts, members_count'])
        with open(f'/mnt/c/Users/user/Desktop/DataAnalyst/DataAnalyst/DataAnalyst/DataMining/VK_API/data + {word}','w',encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=groups_info[0].keys())
            writer.writeheader()
            for gr in groups_info:
                writer.writerow(gr)