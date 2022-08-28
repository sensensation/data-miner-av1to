#by cybersen
#Avito parser data-miner ver 1.1a

import requests
from bs4 import BeautifulSoup as bs
from requests import get 
import time
import random

url = 'https://www.avito.ru/rostov-na-donu/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=3&p='
apartaments = []
print('--*--*--*' * 5)
print('Нажмите клавишу Enter, чтобы начать парсинг')
print('--*--*--*' * 5)

start = input()

print('Внимание! Это тестовая версия программы. В качетсве результата будет выдано первые 6 объявлений!')
print()
time.sleep(2)

count = 1
while count <= 100:
   url = 'https://www.avito.ru/rostov-na-donu/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=3&p=' + str(count)
   print(url)
   response = get(url)
   html_soup = bs(response.text, 'html.parser')

   apartaments_data = html_soup.find_all('div', class_='iva-item-content-rejJg')
   if apartaments_data != []:
      apartaments.extend(apartaments_data)
      value = random.random()
      scaled_value = 1 + (value * (9-5))
      print(f'Задержка: {scaled_value} с.')
      time.sleep(scaled_value)
   else:
      print('Поиск завершен')
      break
   count += 1
  
# print(apartaments[1].text) для отладки
n = int(len(apartaments)) - 1

count = 0
while count <= 5: 
   info = apartaments[int(count)]
   price = info.find('span', {'class':'price-price-JP7qe'}).text
   title = apartaments[count].text
   link = info.find('a')
   link = link.get('href')
   print(f'Объявление №{count+1}')
   print('__' * 10)
   print(f'Описание: {title}')
   print(f'Ссылка на объявление: {link}')
   print(f'Цена: {price}')
   print('__' * 10)
   print(' ')
   count += 1

print(f'Квартир найдено: {n}')

