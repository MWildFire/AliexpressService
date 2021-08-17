from flask import Flask, request, jsonify, make_response
import json
from helper import proxs
from generated import service_pb2_grpc, service_pb2
import grpc
from google.protobuf.json_format import MessageToJson

app = Flask(__name__)


@app.route('/aliexpress-find', methods=['POST'])
def ali_find():
    r = request.get_json(force=True)
    print(r)
    try:
        query = r['query']
    except KeyError:
        return make_response(jsonify({'exc': 'Неверный формат запроса. Необходимо передать query'}))
    try:
        pages = r['pages']
    except KeyError:
        return make_response(jsonify({'exc': 'Неверный формат запроса. Необходимо передать pages'}))
    try:
        proxies = r['proxies']
    except KeyError:
        proxies = proxs
    print(proxies)
    print(type(proxies))
    host = 'localhost'
    server_port = 80
    channel = grpc.insecure_channel(
        '{}:{}'.format(host, server_port))
    stub = service_pb2_grpc.SearchServiceStub(channel=channel)
    message = service_pb2.SearchRequest(query=query, pages=pages, proxies=proxies)
    print(f'{message}')
    json_obj = None
    for r in stub.Search(message):
        json_obj = str(MessageToJson(r))
    json_obj = json.loads(json_obj)
    for i in range(len(json_obj)):
        json_obj['result'][i]['title'] = json_obj['result'][i]['title'].encode('utf-8').decode('utf-8')
        json_obj['result'][i]['desc'] = json_obj['result'][i]['desc'].encode('utf-8').decode('utf-8')
        json_obj['result'][i]['url'] = json_obj['result'][i]['url'].encode('utf-8').decode('utf-8')
        json_obj['result'][i]['price'] = json_obj['result'][i]['price'].encode('utf-8').decode('utf-8')
        with open('grpc_service.json', 'w', encoding='utf-8') as w_f:
            json.dump(json_obj, w_f, ensure_ascii=False, indent=4)
            print(json_obj)
    return make_response(jsonify(json_obj))


if __name__=='__main__':
    app.run()
