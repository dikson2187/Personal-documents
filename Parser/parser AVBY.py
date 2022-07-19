import requests
from bs4 import BeautifulSoup
import csv



URL = 'https://cars.av.by/kia'
HOST = 'https://cars.av.by'
FILE = 'carsa.csv'
HEDERS = {
    'user':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'accept':'ext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEDERS, params=params)
    return r




def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listing-item__wrap')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('span', class_='link-text') .get_text(strip=True),
            'city': item.find('div', class_='listing-item__location') .get_text(strip=True),
            'link': HOST + item.find('a', class_='listing-item__link') .get('href'),
            'many_by': item.find('div', class_='listing-item__price').get_text(strip=True),
            'many_usd': item.find('div', class_='listing-item__priceusd').get_text(strip=True)

        })
    return cars



def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка','Город!','Ссылка','Цена в рубля!','Цена в долорах!'])
        for item in items:
            writer.writerow([item['title'], item['city'], item['link'], item['many_by'], item['many_usd']])


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = get_content(html.text)
        save_file(cars, FILE)
        print(f'получено {len(cars)} автомобилей')
    else:
        print('Error')


parse()
