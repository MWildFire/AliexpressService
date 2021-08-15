from scrape import proxs
import requests
import concurrent.futures
import socks
import socket


def extract(proxy):
    try:
        print(proxy)
        r = requests.get('https://httpbin.org/ip', proxies={'http': f"socks5://{proxy}", 'https': f"socks5://{proxy}"})
        print(r.json(), ' - working')
    except:
        pass
    return proxy


with concurrent.futures.ThreadPoolExecutor() as exector:
    exector.map(extract, proxs)