import json
from helper import proxs
from generated import service_pb2_grpc, service_pb2
import grpc
from google.protobuf.json_format import MessageToJson
import argparse


class UnaryClient(object):
    """
    Клиент gRPC
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 80

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = service_pb2_grpc.SearchServiceStub(channel = self.channel)

    def get_url(self, query: str, pages: int, proxies = proxs):
        """
        Клиент функция для запроса на gRPC сервер
        """
        message = service_pb2.SearchRequest(query=query, pages=pages, proxies=proxs)
        print(f'{message}')
        json_obj = None
        for r in self.stub.Search(message):
            json_obj = str(MessageToJson(r))
            json_obj = json.loads(json_obj)
        for i in range(len(json_obj)):
            json_obj['result'][i]['title'] = json_obj['result'][i]['title'].encode('utf-8').decode('utf-8')
            json_obj['result'][i]['desc'] = json_obj['result'][i]['desc'].encode('utf-8').decode('utf-8')
            json_obj['result'][i]['url'] = json_obj['result'][i]['url'].encode('utf-8').decode('utf-8')
            json_obj['result'][i]['price'] = json_obj['result'][i]['price'].encode('utf-8').decode('utf-8')
            with open('../grpc_service.json', 'w', encoding='utf-8') as w_f:
                json.dump(json_obj, w_f, ensure_ascii=False, indent=4)

        return json_obj

"""

parser = argparse.ArgumentParser(description='Test')
parser.add_argument("--q", type=str, help="Query for AliExpress parsing")
parser.add_argument("--p", type=int, help="Quantity of parsing pages")
parser.add_argument("--prox", type=list, help="Proxie list", default=None)
args = parser.parse_args()
client = UnaryClient()
print('Создан объект')

if args.prox:
    result = client.get_url(query=args.q, pages=args.p, proxies=args.prox)
else:
    result = client.get_url(query=args.q, pages=args.p)


"""