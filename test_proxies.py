from helper import proxs
import requests
import concurrent.futures
import asyncio
import aiohttp
from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector
import random
import time


async def fetch(url):
    connector = ProxyConnector()
    socks = random.choice(proxs)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, proxy=socks) as response:
            print(await response.text())


async def prox_test(proxy):
    socks = proxy
    print(socks)
    connector = ProxyConnector(proxy_type=ProxyType.SOCKS5,
                               host=proxy.split(':')[0],
                               port=proxy.split(':')[1]
                               )
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get('https://httpbin.org/ip') as response:
            print(await response.json(), '- working')


