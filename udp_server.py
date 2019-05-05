from datetime import datetime
import socket

class udpServer:
    def __init__(self, host, port, max_size=4096):
        self.host, self.port, self.max_size = host, port, max_size
        self.server_address = (self.host, self.port)
        #max message size
        print('Starting the server at ', datetime.now())
        print('Waiting for a client to call.')
        #create UDP socket
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #listen host:port
        server.bind(self.server_address)
        #get data
        data, client = server.recvfrom(max_size)
        print('At ', datetime.now(), client, 'send: ', data)
        server.sendto(b'Got', client)
        server.close()