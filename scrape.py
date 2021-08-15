import requests
from bs4 import BeautifulSoup as bs
import json
import random
from proxie_list import proxs

# Заголовки для GET запросов
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


def get_page_html(page: int, product: str):
    """
    Функция принимает номер страницы и наименование продукта и возвращает HTML(строковый объект) из которого можно достать все продукты
    :param page: Номер страницы
    :param product: Наименование продукта для поиска
    :return:
    """
    url = f"https://aliexpress.ru/af/{product.replace(' ', '-')}.html?trafficChannel=af&d=y&SearchText={product.replace(' ', '+')}&ltype=affiliate&SortType=default&page={page}&CatId=0"
    try:
        proxy = random.choice(proxs)  # Случайный прокси для обхода блокировки
        response = requests.get(url=url,
                                proxies={'http': f"socks5://{proxy}", 'https': f"socks5://{proxy}"},)  # Отправляем GET запрос
        response.raise_for_status()
        print(f"Response status ({url}): {response.status_code}")

    except Exception as err:
        print(f"An error ocurred: {err}")
    html = response.text
    return html


def parse_links(html):
    """
    Принимает HTML документ со страницей после поиска и формирует список URL ссылок на товары
    :param html: строковый объект HTML
    :return: список URL ссылок на товары (list)
    """
    prod_urls = []
    soup = bs(html, 'lxml')
    try:
        # Получаем JSON объект в строковом виде из HTML разметки
        items = str(soup.find_all('script', {'type':'text/javascript'})[5]).split('window.runParams =')[2].split(';')[0]
    except:
        print('Здесь ошибка')
        return
    with open('items.json', 'w', encoding='utf-8') as json_write:
        obj = json.loads(items)
        json.dump(obj, json_write, ensure_ascii=False, indent=4)
        for item in obj['items']:
            product_url = item['productDetailUrl'].replace('//', 'https://', 1)
            prod_urls.append(product_url)
    return prod_urls


def run_parse_links(page, product):
    """
    Функция для запуска процесса поиска ссылок для товаров. Формирует список и JSON файл за один запуск
    :param page: номер страницы для поиска товаров (int)
    :param product: имя товаров (string)
    :return:
    """
    response = get_page_html(page, product)
    prod_urls = parse_links(response)
    return prod_urls
    # print(f"Exception occured: {err}")


def get_product_html(product_url):
    """
    Функция для получения HTML документа с товаром. Необходима для получения более предметной информации о товаре.
    :param product_url: URL ссылка на товар
    :return: HTML документ (str)
    """
    url = product_url
    try:
        proxy = random.choice(proxs)  # Случайный прокси для обхода блокировки
        response = requests.get(url=url,
                                proxies={'http': f"socks5://{proxy}",
                                         'https': f"socks5://{proxy}"}, )  # Отправляем GET запрос
        response.raise_for_status()
        print(f"Response status ({url}): {response.status_code}")

    except Exception as err:
        print(f"An error ocurred: {err}")
    html = response.text
    return html


def parse_product(html: str):
    """
    Функция для парсинга страницы с товаром. Используется стандартный метод find
    :param html: HTML документ (str)
    :return: словарь с ключевыми данными о товаре (dict)
    """
    soup = bs(html, 'lxml')
    # Парсим страничку с продуктом
    desc = soup.find('div', {'class': 'detail-desc-decorate-richtext'}).text
    title = soup.find('div', {'class': 'Product_Name__container__hntp3'}).text
    price = soup.find('div', {'class': 'Product_Price__container__1uqb8 product-price'}).find('span').text
    try:
        rating = soup.find('div', {'class': 'Product_Stars__rating__tfb6k'}).text
    except AttributeError:
        rating = 'Не найден'
    return {
        'title': title,
        'desc': desc,
        'price': price,
        'rating': rating
    }


def run_parse_product(product_url: str):
    """
    Функция для запуска полного поиска по странице. Нужна, как процесс в мультипроцессинге.
    :param product_url: URL ссылка товара (str)
    :return: словарь с ключевыми данными (dict)
    """
    product_dict = parse_product(get_product_html(product_url))
    return {
        'title': product_dict['title'],
        'desc': product_dict['desc'],
        'url': product_url,
        'price': product_dict['price'],
        'rating': product_dict['rating']
    }
