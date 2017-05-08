#!/usr/bin/env python
import sys
from base64 import b64decode

def fxor(s1, s2):
    a = map(lambda x: (ord(x)), s1.decode('hex'))
    b = map(lambda x: (ord(x)), s2.decode('hex'))
    xord = map(lambda x, y: x ^ y, a, b)
    return ''.join(map(chr, xord)).encode('hex')

if __name__ == '__main__':
    print fxor(sys.argv[1], sys.argv[2])
