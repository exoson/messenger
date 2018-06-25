import argparse
import server, client


def run():
    parser = argparse.ArgumentParser(description="Start messenger server or client")
    sub_parsers = parser.add_subparsers()

    server_parser = sub_parsers.add_parser("server", help="Start a messenger server")
    server_parser.add_argument("--workers", help="amount of workers ", type=int,
                               default=2)
    server_parser.add_argument("--port", help="service port", type=int,
                               default=50051)
    server_parser.set_defaults(func=server.run)

    client_parser = sub_parsers.add_parser("client", help="Start a messenger client")
    client_parser.add_argument("--ip", help="the ip to connect to as client", type=str)
    client_parser.set_defaults(func=client.run)

    args = parser.parse_args()
    print(args)
    args.func(args)

if __name__ == "__main__":
    run()

