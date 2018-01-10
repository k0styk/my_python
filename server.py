import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', help='Server ip listening')
    parser.add_argument('port', type=int, help='Server port', default=7777)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    print("ip: {}".format(namespace.ip))
    print("port: {}".format(namespace.port))
