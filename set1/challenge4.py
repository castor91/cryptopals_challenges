#!/usr/bin/env python
from string import printable
from challenge3 import freq, choose, func, english

def func(s):
    s = map(lambda x: (ord(x)), s.decode('hex'))
    MAX = 0
    val = []
    COUNT = english['e'] * len(s) + 1
    for c in xrange(256):
        xord = map(lambda x: x ^ c, s)
        if all(chr(c).lower() in printable for c in xord):
            c_i = sum([1 for x in xord if chr(x).lower() not in english.keys()])
            if MAX < freq(xord) and c_i < COUNT:
                MAX = freq(xord)
                val = xord
                COUNT = c_i
    return val

if __name__ == '__main__':
    f = open('4.txt', 'r')
    result = []
    for s in f.readlines():
        result.append(func(s.replace('\n','')))
    f.close()
    result = filter(None, result)
    print ''.join(map(chr, choose(result)))
