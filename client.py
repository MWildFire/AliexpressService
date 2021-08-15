import os
import service_pb2
import service_pb2_grpc
import time
import grpc
from proxie_list import proxs
from scrape import run_parse_links


def generate_links(page: int, product: str):
    prod_urls = run_parse_links(page, product)
    for i in range(len(prod_urls)):
        req_text = service_pb2.SearchRequest(url=prod_urls[i], proxies=proxs)
        yield req_text


def send_message(stub, product):
    responses = stub.Search(generate_links(1, product))
    print(responses)


def run(product: str):
    with grpc.insecure_channel('localhost:80') as channel:
        stub = service_pb2_grpc.SearchServiceStub(channel)
        send_message(stub=stub, product=product)


if __name__ == '__main__':
    run(product='чехол для iphone')