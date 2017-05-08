#!/usr/bin/env python

def is_ECB(data, block_size=16):
    size = len(data) / block_size
    for i in xrange(size):
        for j in xrange(i+1, size):
            if data[i*block_size: (i+1)*block_size] == data[j*block_size:(j+1)*block_size]: return True
    return False

if __name__ == '__main__':
    f = open('8.txt')
    chiper = [x.replace('\n', '').decode('base64').encode('hex') for x in f.readlines()]
    f.close()

    print filter(is_ECB, chiper)
