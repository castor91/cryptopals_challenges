#!/usr/bin/env python
import sys

printable = 'abcdefghijklmnopqrstuvwxyz \''

def evaluate(s):
    return all(chr(c).lower() in printable for c in s)

def func(s):
    s = map(lambda x: (ord(x)), s.decode('hex'))
    for c in xrange(256):
        xord = map(lambda x: x ^ c, s)
        if evaluate(xord):
            return ''.join(map(chr, xord))
    return None

if __name__ == '__main__':
    print func(sys.argv[1])
