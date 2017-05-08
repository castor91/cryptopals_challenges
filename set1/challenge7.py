#!/usr/bin/env python
from Crypto.Cipher import AES

def decrypt(c, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(c)
    return plaintext.rstrip(b"\x04")

if __name__ == '__main__':
    f = open('7.txt')
    chipertext = ''.join([x.replace('\n','') for x in f.readlines()])
    f.close()
    print decrypt(chipertext.decode('base64'), 'YELLOW SUBMARINE')
