#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('name')
    parser.add_argument ('count', type=int)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    print (namespace)
 
    for _ in range (namespace.count):
        print ("Привет, {}!".format (namespace.name) )
