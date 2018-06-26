import grpc
from concurrent import futures
import time

import messenger_pb2_grpc
import messenger_pb2 as api


class MessengerServicer(messenger_pb2_grpc.MessengerServiceServicer):

    def Send(self, request, context):
        pass

    def Recieve(self, request, context):
        pass

    def Login(self, request, context):
        print("Logged in")
        return api.Response(msg="Shieeet")

    def Logout(self, request, context):
        print("Logged out")
        return api.Response(msg="Shaiiit")


def run(args):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.workers))
    messenger_pb2_grpc.add_MessengerServiceServicer_to_server(
        MessengerServicer(), server)
    server.add_insecure_port("[::]:" + str(args.port))
    server.start()
    while 1:
        time.sleep(5)

