# Парсер aliexpress.com
## Описание
HTTP сервер, принимающий POST запрос и собирающий данные из объявлений AliExpress
## Пример запроса
```
curl --header "Content-Type: application/json"  --request POST --data '{"query":"iphone", "pages":
1, "proxies":["host:port","host:port","host:port","host:port","host:port"]}' http://194.67.116.168:5000/aliexpress-find | jq

```
## Входные данные

- query - поисковой запрос (строка)
- pages - количество страниц (целое число)
- proxies - прокси-сервера для парсинга (список строк опционально) 

## Важно

Тестирование проводилось с пятью рабочими proxy серверами. С таким количеством точно вернётся одна страница с продуктами, больше - включится проверка на робота, поэтому лучше проводить тестирование, указывая много прокси серверов в списке прокси.

Flask приложение делает запрос на gRPC сервер и предоставляет ответ в формате JSON. Также реализован клиент для прямого запроса на gRPC приложение