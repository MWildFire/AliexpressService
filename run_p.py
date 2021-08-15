import concurrent.futures
import time
from scrape import run_parse_links, run_parse_product
import json


def get_item_data(search: str):
    """
    Получает поисковой запрос. Выполняет две мультипроцессовых задачи последовательно.
    :param search: Товар для поиска
    :return: JSON объект требуемого формата
    """
    """
    with concurrent.futures.ThreadPoolExecutor() as exector:
        results = []
        for i in range(1):
            results.append(exector.submit(run_parse_links, i, search))
            time.sleep(1)

        for f in concurrent.futures.as_completed(results):
            print(f.result())
            with open('product_urls.json', 'w', encoding='utf-8') as w_f:
                json.dump(f.result(), w_f, ensure_ascii=False, indent=4)
    """
    with open('result.json', 'w', encoding='utf-8') as w_f:
        base = {
                    "search": search,
                    "result":
                    [

                    ]
                }

        json.dump(base, w_f,  ensure_ascii=False, indent=4)
    with concurrent.futures.ThreadPoolExecutor() as exector:
        with open('product_urls.json', 'r', encoding='utf-8') as r_f:
            product_urls = json.load(r_f)

        results = []
        for i in range(len(product_urls[:4])):
            results.append(exector.submit(run_parse_product, product_urls[i]))

        for f in concurrent.futures.as_completed(results):
            print(f.result())
            with open('result.json', 'r', encoding='utf-8') as r_f:
                result = json.load(r_f)
                result['result'].append(f.result())
            with open('result.json', 'w', encoding='utf-8') as w_f:
                json.dump(result, w_f, ensure_ascii=False, indent=4)

    return result
