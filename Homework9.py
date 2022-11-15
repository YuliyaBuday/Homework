import cards as cards
import items as items
import requests
from bs4 import BeautifulSoup
import json

JSON = "cards.json"
HOST = "https://www.lamoda.by/"
URL = "https://www.lamoda.by/c/127/shoes-sandalii/"
HEADERS = {
    'accept': '*/*',
    'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 '
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_ = 'x-product-card__card')
    cards = []

    for item in items:
        cards.append(
             {
                'title': item.find('div', class_ ="x-product-card-description__product-name").get_text(),
                'brand': item.find('div', class_ ="x-product-card-description__brand-name").get_text(),
                'price': item.find('div', class_ ="x-product-card-description__microdata-wrap").get_text(strip=True),
             }
        )
    return cards

def save_doc(items,path):
    with open (path, 'w') as file:
        json.dump(items,file, indent=3, ensure_ascii=False)

def parser ():
    PAGENATION = input('Укажите количество страниц для парсинга:')
    PAGENATION = int(PAGENATION.strip())
    html= get_html(URL)
    if html.status_code==200:
        cards=[]
        for page in range (1, PAGENATION):
            html= get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            print(f'Спарсили страницу:{page}')
            save_doc(cards,JSON)
    else:
        print('Error')

parser()
