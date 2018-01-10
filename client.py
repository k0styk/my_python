# Программа клиента, запрашивающего текущее время

import sys
import argparse
from socket import *
import json
import time


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', help='Server ip address')
    parser.add_argument('port', nargs='?', type=int, help='Server port', default=7777)

    return parser


def to_json_ascii(argument):
    result = json.dumps(argument)

    return result.encode('ascii')


def from_json_ascii(argument):

    result = json.loads(argument.decode('ascii'))

    return result


if __name__ == '__main__':
    parser = create_parser()
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

    print("Connecting to server:")
    print("ip: {}".format(arguments.addr))
    print("port: {}".format(arguments.port))
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((arguments.addr, arguments.port))   # Соединиться с сервером
    s.send(to_json_ascii(presence))
    tm = s.recv(1024)                # Принять не более 1024 байтов данных
    s.close()
    print("Ответ от сервера: %s" % from_json_ascii(tm))
