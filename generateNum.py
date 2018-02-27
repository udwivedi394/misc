import time

def generate(A):
    while 1:
        for i in xrange(A):
            print i,
        print
        time.sleep(0.2)
            for j in xrange(A,0,-1):
            print j,
        print

generate(10)
