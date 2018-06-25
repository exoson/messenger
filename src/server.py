import grpc
from concurrent import futures
import time

import messenger_pb2, messenger_pb2_grpc


class MessengerServicer(messenger_pb2_grpc.MessengerServiceServicer):

    def Send(self, request, context):
        pass

    def Recieve(self, request, context):
        pass

    def Login(self, request, context):
        print("Logged in")
        return messenger_pb2.Response(msg="Shieeet")

    def Logout(self, request, context):
        pass


def run(args):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.workers))
    messenger_pb2_grpc.add_MessengerServiceServicer_to_server(
        MessengerServicer(), server)
    server.add_insecure_port("[::]:" + str(args.port))
    server.start()
    while 1:
        time.sleep(5)

