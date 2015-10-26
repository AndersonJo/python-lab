from unittest import TestCase
from gevent import socket
import struct


class SocketTest(TestCase):
    def test_server(self):
        sock = socket.create_connection(('localhost', 5001))
        self.send_msg(sock, 'Hi')
        self.send_msg(sock, 'This is Chang Min')
        sock.close()

    def send_msg(self, sock, msg):
        msg = msg.encode('UTF-8')
        packed = struct.pack('>I', len(msg))
        sock.send(packed + msg)
