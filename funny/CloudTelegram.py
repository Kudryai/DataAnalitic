# Обработка JSON файла Telegram, очистка от стоп-слов и формирование файла txt, 
# для дальнейшего создания облака слов.

import json
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

tgu = open('/mnt/c/Users/user/Desktop/DataAnalyst/DataAnalyst/DataAnalyst/funny/result2.json', 'r', encoding = 'utf-8')
tgu = json.load(tgu)
mas = []

for txt in tgu['messages']:
    mas.append(txt['text'])
stroka = ''
for i in mas:
    i = str(i).lower()
    for j in i:
        if j.isalpha() or j == ' ' or j == '-' :
            stroka = stroka.strip('abcdefgjklmnoprstqwzxuihyvo-')
            stroka += j.replace(",", " ")
data = stroka.split()
stop_words = open('/mnt/c/Users/user/Desktop/DataAnalyst/DataAnalyst/DataAnalyst/funny/stop-ru.txt', 'r', encoding='utf8')
stop_words1 = stop_words.read()
stop_words1 = stop_words1.split('\n')
stop_words.close()
clear_data=[]
for zz in data:
    if(zz not in stop_words1):
        clear_data.append(zz)

result = ''
for norm in clear_data:
    if 10 > len(norm) > 4:
        if norm not in 'abcdefgjklmnoprstqwzxui':
            result += norm + ' '
res = open('/mnt/c/Users/user/Desktop/DataAnalyst/DataAnalyst/DataAnalyst/funny/out2.txt', 'w', encoding = 'utf-8')
res.write(result)
res.close()

