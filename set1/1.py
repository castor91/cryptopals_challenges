#!/usr/bin/env python
from base64 import b64encode, b64decode
import sys

def hex2b64(msgH):
    msgS = ''.join(map(lambda x: chr(ord(x)), msgH.decode('hex')))
    return b64encode(msgS)

if __name__ == '__main__':
    print hex2b64(sys.argv[1])
