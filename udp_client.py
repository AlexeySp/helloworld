import socket
from datetime import datetime

class udpClient:
    def __init__(self, host, port, max_size = 4096):
        self.host, self.port, self.max_size = host, port, max_size
        server_address = (self.host, self.port)
        print('Starting the client at ', datetime.now())
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(b'Hey!', server_address)
        data, server = client.recvfrom(max_size)
        print('At ', datetime.now(), server, 'said', data)
        client.close()