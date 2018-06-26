import grpc

import messenger_pb2_grpc
import messenger_pb2 as api

def run(args):
    channel = grpc.insecure_channel(args.ip)
    stub = messenger_pb2_grpc.MessengerServiceStub(channel)

    running = True
    session_id = ""
    while running:
        cmd = input("Input command: ")
        if cmd.startswith("user"):
            session_id = stub.Login(api.LoginRequest(user_id=cmd.split(":")[1])).msg
            print(session_id)

