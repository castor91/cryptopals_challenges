#!/usr/bin/env python
import sys
import random
import challenge9
from Crypto.Cipher import AES
sys.path.append('../set1')
from challenge8 import is_ECB

def random_string_len(a, b):
    return random_string(random.randint(a, b))

def random_string(length=16):
    return ''.join([chr(random.randint(0, 255)) for _ in xrange(length)])


def encrypt_AES_ECB(data, key):
    data = challenge9.pack_pkcs7(data, 16)
    chiper = AES.new(key, AES.MODE_ECB)
    return chiper.encrypt(data)


def encrypt_AES_CBC(data, key):
    data = challenge9.pack_pkcs7(data, 16)
    chiper = AES.new(key, AES.MODE_CBC, random_string())
    return chiper.encrypt(data)


def encryption_oracle(data):
    choose = random.randint(0, 1)
    key = random_string(16)
    data = random_string_len(5,10) + data + random_string_len(5,10)
    if choose == 0:
        result = encrypt_AES_ECB(data, key)
    else:
        result = encrypt_AES_CBC(data, key)

    return result, 'AES_ECB' if choose == 0 else 'AES_CBC'

if __name__ == '__main__':
    N = 100
    result = 0
    f = open('input.txt', 'r')
    input = ''.join([x for x in f.readlines()])
    f.close()
    for _ in xrange(N):
        test_chiper, mode = encryption_oracle(input)
        # print test_chiper
        if is_ECB(test_chiper):
            result += int(mode == 'AES_ECB')
        else:
            result += int(mode == 'AES_CBC')
    print 'Result:  right {}/{}'.format(result, N)
