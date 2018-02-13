#https://www.interviewbit.com/problems/min-xor-value/
INF = 10**10
def findMinXor(A):
    A.sort()
    n = len(A)
    mini = INF
    for i in xrange(n-1):
        mini = min(mini,A[i]^A[i+1])

    return mini

A = [0,2,5,7]
print findMinXor(A)

A = [0,4,7,9]
print findMinXor(A)
