#!/usr/bin/env python
import sys
from string import printable

english = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07}

def freq(s):
    f = {chr(x).lower() : s.count(x) / float(len(s)) for x in s}
    res = sum([abs(english[k] - v) for k,v in f.iteritems() if k in english])
    return res

# Make refactoring
def choose(l):
    MAX = 0
    COUNT = int(english['e'] * len(l[0])) + 1
    val = []

    for xord in l:
        if all(chr(c).lower() in printable for c in xord):
            c_i = sum([1 for x in xord if chr(x).lower() not in english.keys()])
            if MAX < freq(xord) and c_i < COUNT:
                MAX = freq(xord)
                val = xord
                COUNT = c_i

    return val, l.index(val)

def func(s):
    s = map(lambda x: (ord(x)), s.decode('hex'))
    l = []
    for c in xrange(256):
        l.append(map(lambda x: x ^ c, s))
    return ''.join(map(chr, choose(l)[0]))

if __name__ == '__main__':
    print func(sys.argv[1])
