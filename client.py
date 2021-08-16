import json

import service_pb2
import service_pb2_grpc
import grpc
from google.protobuf.json_format import MessageToJson


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 80

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = service_pb2_grpc.SearchServiceStub(channel = self.channel)

    def get_url(self, query: str, pages: int):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = service_pb2.SearchRequest(query=query, pages=pages)
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
        with open('grpc_service.json', 'w', encoding='utf-8') as w_f:
            json.dump(json_obj, w_f, ensure_ascii=False, indent=4)
            print(json_obj)
        return


if __name__ == '__main__':
    client = UnaryClient()
    result = client.get_url(query='ipad pro', pages=1)


