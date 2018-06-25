import argparse
from src import server, client


def run():
    parser = argparse.ArgumentParser(description="Start messenger server or client")
    parser.add_argument("mode", choices=["server", "client"])
    parser.add_argument("--ip", help="the ip to connect to as client", type=str)
    args = parser.parse_args()
    print(args)
    if args.mode == "server":
        server.run(args)
    elif args.mode == "client":
        client.run(args)

if __name__ == "__main__":
    run()

