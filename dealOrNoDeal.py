#Nest away

import sys

def dealorNoDeal05(A,B):
    lookup = [B-i for i in A]
    maxi = 0
    for i in xrange(1,len(lookup)):
        if lookup[i] >= 0:
            lookup[i] = lookup[i]+(lookup[i-1] if lookup[i-1] >=0 else 0)
            maxi = max(maxi,lookup[i])
    return maxi

def dealorNoDeal(A,B):
    lookup = A#[B-i for i in A]
    maxi = 0
    for i in xrange(len(lookup)):
        lookup[i] = max(lookup[i],lookup[i]+lookup[i-1] if i>0 else 0)
        maxi = max(maxi,lookup[i])
    return maxi

def dealorNoDeal03(A,B):
    lookup = A
    for i in xrange(len(lookup)):
        lookup[i] = B-lookup[i]
    maxi = 0
    for i in xrange(1,len(lookup)):
        if lookup[i] >= 0:
            lookup[i] = lookup[i]+(lookup[i-1] if lookup[i-1] >=0 else 0)
            maxi = max(maxi,lookup[i])
    return maxi

def dealorNoDeal04(A,B):
    lookup = A
    maxi = 0
    for i in xrange(len(lookup)):
        if B-lookup[i] >= 0:
            lookup[i] = (B-lookup[i])+(lookup[i-1] if i > 0 and lookup[i-1] >=0 else 0)
            maxi = max(maxi,lookup[i])
        else:
            lookup[i] = B-lookup[i]
    print lookup
    return maxi
"""
if __name__=="__main__":
    f1 = open("testCaseMaxSeq02.txt",'r')
    for x in xrange(int(f1.readline().strip())):
        #n,c = map(int,sys.stdin.readline().strip().split())
        n = map(int,f1.readline().strip().split())
        A = map(int,f1.readline().strip().split())
        c = 0
        result = dealorNoDeal(A,c)
        sys.stdout.write(str(result))
        print
    f1.close()
"""

if __name__=="__main__":
    for x in xrange(int(sys.stdin.readline().strip())):
        n,c = map(int,sys.stdin.readline().strip().split())
        #n = map(int,sys.stdin.readline().strip().split())
        A = map((lambda x: c-int(x)),sys.stdin.readline().strip().split())
        #c = 0
        result = dealorNoDeal(A,c)
        sys.stdout.write(str(result))
        print
#"""
