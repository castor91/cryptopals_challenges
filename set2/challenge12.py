#!/usr/bin/env python
import sys
import challenge11
import string
import challenge9

key = challenge11.random_string()

def oracle_function(data):
    to_append = \
'''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''
    return challenge11.encrypt_AES_ECB(data + to_append.decode('base64'), key)

if __name__ == '__main__':

    # Step 1
    block_size = 0
    while True:
        result = oracle_function('A' * block_size)
        if challenge11.is_ECB(result): break
        block_size += 1
    block_size /= 2
    print 'Step #1: Block size length = {}'.format(block_size)

    # Step 2
    if challenge11.is_ECB(oracle_function('A' * block_size * 4)):
        print 'Step #2: Detect AES ECB mode'

    # Step 3-4-5-6
    result = ''
    block_size *= 8
    for i in xrange(1, block_size + 1):
        input_block = 'A' * (block_size - i) + (result if len(result) < block_size else result[-block_size:])
        possible = {oracle_function(input_block + x)[:block_size].encode('hex') : (input_block + x) for x in string.printable}
        # I don't need this
        tmp = challenge9.pack_pkcs7(input_block, block_size)
        possible.update({oracle_function(tmp) : tmp})

        if len(result) == block_size: print possible
        first_char_block = oracle_function(input_block[:block_size- i])[:block_size].encode('hex')
        result = possible[first_char_block][block_size - i:]

    print 'Step #3:\n{}'.format(result)
