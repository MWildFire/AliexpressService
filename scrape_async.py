import requests
from bs4 import BeautifulSoup as bs
import json
import random
import aiohttp
import asyncio
from helper import proxs, get_cookies
from aiohttp_socks import ProxyType, ProxyConnector
import time

# Заголовки для GET запросов
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


async def get_page_html(page: int, product: str, proxies: list):
    """
    Функция принимает номер страницы и наименование продукта и возвращает HTML(строковый объект) из которого можно достать все продукты
    :param page: Номер страницы
    :param product: Наименование продукта для поиска
    :return:
    """
    url = f"https://aliexpress.ru/af/{product.replace(' ', '-')}.html?trafficChannel=af&d=y&SearchText={product.replace(' ', '+')}&ltype=affiliate&SortType=default&page={page}&CatId=0"
    try:
        proxy = random.choice(proxies)  # Случайный прокси для обхода блокировки
        connector = ProxyConnector(proxy_type=ProxyType.SOCKS5,
                                   host=proxy.split(':')[0],
                                   port=proxy.split(':')[1]
                                   )
        async with aiohttp.ClientSession(connector=connector) as session:

            async with session.get(url=url,
                                   cookies=get_cookies(),
                                   headers=header) as response:  # Отправляем GET запрос
                response.raise_for_status()
                print(f"Response status ({url}): {response.status}")
                return await response.text()
    except Exception as err:
        print(f"An error ocurred: {err}")


async def parse_links(page: int, product: str, proxies: list = proxs):
    """
    Принимает HTML документ со страницей после поиска и формирует список URL ссылок на товары
    :param html: строковый объект HTML
    :return: список URL ссылок на товары (list)
    """
    prod_urls = []
    html = await get_page_html(page, product, proxies)
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
        try:
            for item in obj['items']:
                product_url = item['productDetailUrl'].replace('//', 'https://', 1)
                prod_urls.append(product_url)
        except KeyError:
            return prod_urls

    return prod_urls


async def get_product_html(product_url , proxies: list):
    """
    Функция для получения HTML документа с товаром. Необходима для получения более предметной информации о товаре.
    :param product_url: URL ссылка на товар
    :return: HTML документ (str)
    """
    url = product_url
    try:
        proxy = random.choice(proxies)  # Случайный прокси для обхода блокировки
        connector = ProxyConnector(proxy_type=ProxyType.SOCKS5,
                                   host=proxy.split(':')[0],
                                   port=proxy.split(':')[1]
                                   )
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url=url,
                                   cookies=get_cookies(),
                                   headers=header) as response:  # Отправляем GET запрос
                response.raise_for_status()
                print(f"Response status ({url}): {response.status}")
                return await response.text()
    except Exception as err:
        print(f"An error ocurred: {err}")


async def parse_product(product_url: str, proxies: list = proxs):
    """
    Функция для парсинга страницы с товаром. Используется стандартный метод find
    :param html: HTML документ (str)
    :return: словарь с ключевыми данными о товаре (dict)
    """
    html = await get_product_html(product_url, proxies)
    soup = bs(html, 'lxml')

    # Парсим страничку с продуктом
    try:
        script = soup.findAll('script')[13]
        if len(str(script)) < 100:
            raise IndexError
    except IndexError:
        script = soup.findAll('script')[14]
    str_data = str(script).split('window.runParams = ')[1].split(';')[0].split('data:')[1].split(',"shippingModule":{')[0]+'}'

    with open('product_data_test.json', 'w', encoding='utf-8') as w_f:
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

"""
if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    prod_urls = loop.run_until_complete(parse_product('https://aliexpress.ru/item/1005001625499669.html?s=p&ad_pvid=20210816085716690131346798440022207110_1&algo_pvid=597a805f-c100-4076-ac1e-1711e45c95ed&algo_expid=597a805f-c100-4076-ac1e-1711e45c95ed-0&btsid=0b8b15cb16291294363335330eda1a&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_'))

    print(prod_urls)



async def main():

    print("Creating new task")
    urls = await asyncio.gather(*[parse_links(i, 'чехол iphone') for i in range(1, 3)])
    #  urls = await parse_links(1, 'чехол iphone')
    print(await asyncio.gather(*[parse_product(url) for url in urls[1][:5]]))




if __name__ == '__main__':
    asyncio.run(main())

"""