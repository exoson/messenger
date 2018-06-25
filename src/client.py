import grpc

import messenger_pb2_grpc

def run(args):
    channel = grpc.insecure_channel(args.ip)
    stub = messenger_pb2_grpc.MessengerServiceStub(channel)

    running = True
    session_id = ""
    while running:
        cmd = input("Input command: ")
        if cmd.startswith("user"):
            stub.Login(cmd.split(":")[1])

