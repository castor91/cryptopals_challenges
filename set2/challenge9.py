#!/usr/bin/env python
import sys

pack_pkcs7 = lambda data, block_size: data + (block_size - len(data) % block_size) * \
    chr(block_size - len(data) % block_size)
unpack_pkcs7 = lambda data: data[:-ord(data[len(data) - 1:])]

if __name__ == '__main__':
    print pack_pkcs7(' '.join(sys.argv[1:]), 20)
