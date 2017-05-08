#!/usr/bin/env python
import sys
import challenge9
sys.path.append('../set1')
from challenge7 import decrypt

def decrypt_AES_CBC(data, key, IV=b'\x00'*16, size=16):
    blocks = [data[i * size: (i+1)*size] for i in xrange(len(data) / size + 1)]
    result = []
    tmp_IV = IV
    for b in filter(None, blocks):
        tmp = map(lambda x, y: chr(ord(x) ^ ord(y)), decrypt(b, key), tmp_IV)
        result.append(tmp)
        tmp_IV = b
    return ''.join(map(lambda x: ''.join(x), result))


if __name__ == '__main__':
    f = open('10.txt', 'r')
    chiper = ''.join([x.replace('\n', '') for x in f.readlines()]).decode('base64')
    f.close()
    print challenge9.unpack_pkcs7(decrypt_AES_CBC(chiper, 'YELLOW SUBMARINE'), 16)
