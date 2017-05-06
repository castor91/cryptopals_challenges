#!/usr/bin/env python
from base64 import b64decode
import challenge3

def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    l1 = ''.join(['{:08b}'.format(ord(x)) for x in s1])
    l2 = ''.join(['{:08b}'.format(ord(x)) for x in s2])
    return sum([1 for x in xrange(len(l1)) if l1[x] != l2[x]])

def guess_KEYSIZE(c, length=1, average=1): #TODO average
    KEYSIZE_SORTED = [(KEYSIZE, sum([hamming_distance(c[i*KEYSIZE:(i+1)*KEYSIZE], c[(i+1)*KEYSIZE:(i+2)*KEYSIZE]) for i in xrange(average)]) / float(KEYSIZE)) for KEYSIZE in xrange(2, 41)]
    return sorted(KEYSIZE_SORTED, key=lambda x: x[1])[:length]

if __name__ == '__main__':
    f = open('6.txt', 'r')
    text_coded = ''.join(map(lambda x: x.replace('\n', ''), f.readlines()))
    f.close()
    text = b64decode(text_coded)
    KEYSIZEs = guess_KEYSIZE(text, length=3, average=10)
    for size, value in KEYSIZEs:
        print 'Test {:02} length with {:2f} value ...'.format(size, value),
        blocks = [text[i * size:(i+1)*size] for i in xrange(0, len(text) / size)]
        transpose = map(lambda x: ''.join(x), zip(*blocks))
        transpose = [[ord(x) for x in t] for t in transpose]
        result = []
        for t in transpose:
            l = []
            for c in xrange(256):
                l.append(map(lambda x: x ^ c, t))
            result.append(challenge3.choose(l))
        result = filter(None, result)
        if len(result) == size:
            print 'successful!\n{}'.format(''.join([''.join(map(lambda y: chr(y), x)) for x in zip(*result)]))
            break
        else:
            print 'fail'
