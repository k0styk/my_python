# Программа клиента, запрашивающего текущее время

import sys
import argparse
from socket import *

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', help='Server ip address')
    parser.add_argument('port', nargs='?', type=int, help='Server port', default=7777)

    return parser


if __name__ == '__main__':
    parser = createParser()
    arguments = parser.parse_args(sys.argv[1:])

    print("Try to connect:")
    print("ip: {}".format(arguments.addr))
    print("port: {}".format(arguments.port))
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((arguments.addr, arguments.port))   # Соединиться с сервером
    tm = s.recv(1024)                # Принять не более 1024 байтов данных
    s.close()
    print("Текущее время: %s" % tm.decode('ascii'))