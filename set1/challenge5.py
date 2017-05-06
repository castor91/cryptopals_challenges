#!/usr/bin/env python
import sys

def encr(msg, key="ICE"):
    msg = [ord(x) for x in msg]
    print msg
    result = ''
    for i in xrange(len(msg)):
        result += '{:02x}'.format(msg[i] ^ ord(key[i % len(key)]))
    return result


if __name__ == '__main__':
    msg = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
    print encr(msg)

