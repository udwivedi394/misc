#https://www.interviewbit.com/problems/number-of-1-bits/

def numSetBits(A):
    count = 0
    for i in xrange(64):
        if (A&1):
            count += 1
        A >>= 1
    return count

A = 11
print numSetBits(A)
