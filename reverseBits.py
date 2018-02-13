#https://www.interviewbit.com/problems/reverse-bits/
def reversebits(A):
    num = 0
    for i in xrange(31,-1,-1):
        num += (A&1)<<i
        A >>= 1
    return num

print reversebits(3)
