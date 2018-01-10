# Программа сервера времени

import sys
import argparse
from socket import *
import time

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', nargs='?', help='Server ip listening', default='')
    parser.add_argument('-p', '--port', nargs='?', type=int, help='Server port', default=7777)

    return parser


if __name__ == '__main__':
    parser = createParser()
    arguments = parser.parse_args(sys.argv[1:])

    print("Server running on:")
    print("ip: {}".format(arguments.addr))
    print("port: {}".format(arguments.port))
    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP

    s.bind((arguments.addr, arguments.port))                # Присваивает порт 8888
    s.listen(5)                       # Переходит в режим ожидания запросов;
                                      # одновременно обслуживает не более
                                      # 5 запросов.
    while True:
        client, addr = s.accept()     # Принять запрос на соединение
        print("Получен запрос на соединение от %s" % str(addr))
        
        timestr = time.ctime(time.time()) + "\n"
        
        # Обратите внимание, дальнейшая работа ведётся с сокетом клиента
        client.send(timestr.encode('ascii'))   # <- По сети должны передаваться байты,
                                               # поэтому выполняется кодирование строки 
        client.close()