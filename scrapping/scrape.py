import requests
from bs4 import BeautifulSoup as bs
import json
import random
from helper import proxs, get_cookies

# Заголовки для GET запросов
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


def get_page_html(page: int, product: str, proxies: list):
    """
    Функция принимает номер страницы и наименование продукта и возвращает HTML(строковый объект) из которого можно достать все продукты
    :param page: Номер страницы
    :param product: Наименование продукта для поиска
    :return:
    """
    url = f"https://aliexpress.ru/af/{product.replace(' ', '-')}.html?trafficChannel=af&d=y&SearchText={product.replace(' ', '+')}&ltype=affiliate&SortType=default&page={page}&CatId=0"
    try:
        proxy = random.choice(proxies)  # Случайный прокси для обхода блокировки
        response = requests.get(url=url,cookies=get_cookies(), headers=header,proxies={'htttp' : f'socks5://{proxy}', 'htttps' : f'socks5://{proxy}'})
        response.raise_for_status()
        print(response.text)
        print(f"{url} {response.status_code}")

        return response.text
    except Exception as e:
        print(e)
        return ''


def parse_links(page: int, product: str, proxies: list = proxs):
    """
    Принимает HTML документ со страницей после поиска и формирует список URL ссылок на товары
    :param html: строковый объект HTML
    :return: список URL ссылок на товары (list)
    """
    prod_urls = []
    html = get_page_html(page, product, proxies)
    if len(html) == 0:
        return []
    soup = bs(html, 'lxml')
    try:
        script = soup.find_all('script', {'type':'text/javascript'})[5]
    except IndexError:
        return []
    print(script)
    try:
        # Получаем JSON объект в строковом виде из HTML разметки
        items = str(script).split('window.runParams =')[2].split('};')[0]+'}'
        print(items)
    except:
        print('Здесь ошибка')
        return []

    with open('../items.json', 'w', encoding='utf-8') as json_write:
        obj = json.loads(items)
        json.dump(obj, json_write, ensure_ascii=False, indent=4)
        try:
            print('Ищем ссылки по JSON')
            for item in obj['items']:
                product_url = item['productDetailUrl'].replace('//', 'https://', 1)
                prod_urls.append(product_url)
        except KeyError:
            return prod_urls

    return prod_urls


def get_product_html(product_url , proxies: list):
    """
    Функция для получения HTML документа с товаром. Необходима для получения более предметной информации о товаре.
    :param product_url: URL ссылка на товар
    :return: HTML документ (str)
    """
    url = product_url
    try:
        proxy = random.choice(proxies)  # Случайный прокси для обхода блокировки
        response = requests.get(url=url, cookies=get_cookies(), headers=header,
                                proxies={'htttp': f'socks5://{proxy}', 'htttps': f'socks5://{proxy}'})
        response.raise_for_status()
        print(f"{url} {response.status_code}")
        return response.text
    except Exception as e:
        print(e)
        return ''


def parse_product(product_url: str, proxies: list = proxs):
    """
    Функция для парсинга страницы с товаром. Используется стандартный метод find
    :param html: HTML документ (str)
    :return: словарь с ключевыми данными о товаре (dict)
    """
    html = get_product_html(product_url, proxies)

    if len(html) == 0:
        return []
    soup = bs(html, 'lxml')
    if len(soup.findAll('script')) > 10:
        # Парсим страничку с продуктом
        try:
            script = soup.findAll('script')[13]
            print(script)
            if len(str(script)) < 100:
                raise IndexError
        except IndexError:
            script = soup.findAll('script')[15]


        str_data = str(script).split('window.runParams = ')[1].split('};')[0].split('data:')[1].split(',"shippingModule":{')[0]+'}'


        with open('../product_data_test.json', 'w', encoding='utf-8') as w_f:
            data = json.loads(str_data)
            json.dump(data, w_f, ensure_ascii=False, indent=4)

        price = data["priceModule"]["formatedPrice"]
        title = data["pageModule"]["title"]
        desc = data["pageModule"]["description"]
        link = data["pageModule"]["mSiteUrl"]

        return {
            'title': title,
            'desc': desc,
            'price': price,
            'url': link
        }
    else:
        print(soup)
        return {
            'title': soup.find('div', {'class': 'Product_Name__container__hntp3'}).text,
            'desc': soup.find('div', {'class': 'ProductDescription-module_content__1xpeo'}).text,
            'price': soup.find('div', {'class': 'Product_Price__container__1uqb8 product-price'}).text,
            'url': product_url
        }

