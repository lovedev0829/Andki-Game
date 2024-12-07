import socket
import time
import json
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.140.150"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except Exception as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)
    
    # def sendjson(self, data):
        # data = f"json:{json.dumps(data)}".encode('utf-8')
        # try:
            # self.client.send(data)
            # return json.loads(self.client.recv(2048*2))
        # except socket.error as e:
            # print(e)
