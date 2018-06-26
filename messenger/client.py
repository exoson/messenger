import grpc
import threading

import messenger_pb2_grpc
import messenger_pb2 as api


class ClientHandler():

    def __init__(self, args):
        """Init client handler"""
        self.channel = grpc.insecure_channel(args.ip)
        self.stub = messenger_pb2_grpc.MessengerServiceStub(self.channel)
        self.COMMANDS = {
            "login": self.login,
            "logout": self.logout,
            "msg": self.send_msg,
        }
        self.session_id = None

    def parse_command(self, cmd):
        """Run command"""
        split_cmd = cmd.split(":", 2)
        try:
            self.COMMANDS[split_cmd[0]](split_cmd[1])
        except KeyError:
            pass

    def login(self, args):
        """Login to server"""
        if self.session_id is None:
            self.user_id = args
            self.session_id = self.stub.Login(api.LoginRequest(user_id=args)).msg
            self.receive_thread = threading.Thread(target=self.recieve_msgs,
                                                   daemon=True)
        else:
            print("Already logged in.")

    def logout(self, args):
        """Logout from server"""     
        if self.session_id is not None:
            self.stub.Logout(api.LogoutRequest(user_id=self.user_id))
            self.session_id = None
          
        else:
            print("Already not logged in.")
           
        

    def recieve_msgs(self):
        """Recieve messages from server"""
        recv_req = api.RecieveRequest(user_id=self.user_id,
                                      session_id=self.session_id)
        for msg in self.stub.Recieve(recv_req):
            pass

    def send_msg(self, args):
        """Send message to server"""
        
        response = self.stub.Send(api.ChatMessage(msg=args, sender=self.user_id, session_id=self.session_id )).msg
        print(response)
        


def run(args):
    client_handler = ClientHandler(args)

    running = True
    while running:
        cmd = input("Input command: ")
        client_handler.parse_command(cmd)
        if cmd == "exit":
            running = False

