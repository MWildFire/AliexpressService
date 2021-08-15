from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc
import time
import threading
from scrape import run_parse_product


class Listener(service_pb2_grpc.SearchServiceServicer):

    def __init__(self, *args, **kwargs):
        self.result_list = []

    def Search(self, request_iterator, context):
        for message in request_iterator:
            response = service_pb2.SearchResponseStream()
            resp_item = service_pb2.ResponseItem()
            url = message.url
            res = run_parse_product(url)
            resp_item.title = res['title']
            resp_item.desc = res['desc']
            resp_item.url = url
            resp_item.price = res['price']
            resp_item.rating = res['rating']
            response.query = message.query
            self.result_list.append(resp_item)
            response.result = self.result_list
            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_SearchServiceServicer_to_server(Listener(), server)
    server.add_insecure_port('[::]:80')
    server.start()
    try:
        while True:
            print('server on: threads %i' % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print('KeyboarInterrupt')
        server.stop(0)


if __name__=='__main__':
    serve()