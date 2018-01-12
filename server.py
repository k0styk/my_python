# Программа сервера времени

import sys
import argparse
from socket import *
import json
import time

'''
response = {
    "response": "1xx / 2xx / 4xx / 5xx",
    "time": timestamp,
    "error": "error message (optional)"
}
'''


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', nargs='?', help='Server ip listening', default='')
    parser.add_argument('-p', '--port', nargs='?', type=int, help='Server port', default=7777)

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

    print("Server running on:")
    print("ip: {}".format(arguments.addr))
    print("port: {}".format(arguments.port))
    s = socket(AF_INET, SOCK_STREAM)

    s.bind((arguments.addr, arguments.port))
    s.listen(5)

    while True:
        client, addr = s.accept()
        print("Получен запрос на соединение от %s" % str(addr))

        data = client.recv(1024)

        print("result: %s" % data.decode('ascii'))
        request = from_json_ascii(data)

        if request['action'] == 'presence':
            timestamp = int(time.time())
            response = {
                "response": "200",
                "time": timestamp,
                "alert": "OK"
            }
            client.send(to_json_ascii(response))
        else:
            timestamp = int(time.time())
            response = {
                "response": "400",
                "time": timestamp,
                "error": "Неправильный запрос"
            }
        client.close()
