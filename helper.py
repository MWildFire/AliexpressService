proxs = [
    '91.132.196.138:45786',
    '45.140.19.26:45786',
    '193.233.74.225:45786',
    '92.118.113.58:45786',
    '185.142.98.60:45786'
]

"""
    '194.116.163.146:45786',
    '94.45.164.172:45786',
    '89.191.227.34:45786',
    '191.96.59.108:45786',
    '64.137.72.159:45786',
    '166.1.9.75:45786',
    '154.16.211.73:45786',
    '181.215.91.93:45786',
    '50.114.84.202:45786',
    '102.129.212.19:45786',
    '134.202.123.11:45786',
    '191.101.148.241:45786',
    '94.124.160.91:45786',
    '181.214.224.99:45786',
    '185.33.84.125:45786',
    '185.170.56.82:45786',
    '64.188.7.158:45786',
    '154.127.48.3:45786',
    '191.101.163.83:45786',
    '166.1.8.206:45786',
    '181.214.223.136:45786',
    '191.101.157.208:45786',
    '181.215.201.153:45786',
    '181.215.29.42:45786',
    '181.215.93.82:45786',
    '181.215.184.190:45786',
    '181.214.96.63:45786',
    '166.1.12.223:45786',
    '64.137.80.91:45786',
    '64.137.24.75:45786',
    '50.114.85.47:45786',
    '181.215.220.178:45786',
    '181.215.185.89:45786'
"""


def get_cookies():
    """
    Получение cookies от авторизированного пользователя AliExpress
    :return: словарь cookies
    """
    cookies = {}
    with open('aliexpress.ru_cookies.txt', 'r', encoding='utf-8') as read_file:
        text_cookies = read_file.read().split('\n')[4:]
        for cookie in text_cookies:
            cookies.update({
                cookie.split('\t')[5]:cookie.split('\t')[6]
            })
        return cookies