import sys

def encr(msg, key="ICE"):
    msgB = map(ord, msg)
    keyB = map(ord, key*(len(msgB) / len(key) + 1)) 

    encrB = map(lambda x, y: x ^ y, msgB, keyB[:len(msgB)])
    encr = ''.join(map(chr, encrB))

    return encr


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Using ./1.5.py msg_to_encr"
        sys.exit(-1)

    print encr(sys.argv[1], "ICE")

