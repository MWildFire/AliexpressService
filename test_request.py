import requests
from helper import proxs



data = {
        'query': 'gucci',
        'pages': 1,
        'proxies': proxs
    }
print(data)
sesssion = requests.Session()
r = sesssion.post('http://194.67.116.168:5000/aliexpress-find', json = data,
                  headers={"content-type": "application/json"}
    )

print(r.json())
