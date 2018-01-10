# Программа клиента, запрашивающего текущее время

import sys
import argparse
from socket import *
import json
import time

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', help='Server ip address')
    parser.add_argument('port', nargs='?', type=int, help='Server port', default=7777)

    return parser


if __name__ == '__main__':
    parser = createParser()
    arguments = parser.parse_args(sys.argv[1:])

    timestamp = int(time.time())

    presence = {
        "action": "presence",
        "time": timestamp,
        "type": "status",
        "user": {
            "account_name": "user1",
            "status": "Yep, I am here!"
        }
    }

    print("Try to connect:")
    print("ip: {}".format(arguments.addr))
    print("port: {}".format(arguments.port))
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((arguments.addr, arguments.port))   # Соединиться с сервером
    tm = s.recv(1024)                # Принять не более 1024 байтов данных
    s.close()
    print("Текущее время: %s" % tm.decode('ascii'))

#     import socket

# sock = socket.socket()
# sock.connect(('localhost', 9090))
# sock.send('hello, world!')

# data = sock.recv(1024)
# sock.close()

# print data