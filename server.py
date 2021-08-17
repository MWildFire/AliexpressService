from concurrent import futures
import grpc
from generated import service_pb2_grpc, service_pb2
from scrapping.scrape import parse_links, parse_product


class Listener(service_pb2_grpc.SearchServiceServicer):

    def Search(self, request, context):

        response = service_pb2.SearchResponseStream()
        resp_item = service_pb2.ResponseItem()
        for j in range(1, request.pages+1):
            list_links = parse_links(product=request.query, page=j, proxies=request.proxies)
            print(len(list_links))

            for i in range(len(list_links)):
                data = parse_product(list_links[i])
                if type(data) == list:
                    yield response
                # print(data)
                resp_item.title = data['title']
                resp_item.desc = data['desc']
                resp_item.url = data['url']
                resp_item.price = data['price']
                response.query = request.query
                response.page = request.pages
                print(resp_item)
                response.result.append(resp_item)
                yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_SearchServiceServicer_to_server(Listener(), server)

    server.add_insecure_port('[::]:80')
    server.start()
    server.wait_for_termination()


if __name__=='__main__':
    serve()