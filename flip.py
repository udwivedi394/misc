#https://www.interviewbit.com/problems/flip/

def xor(a):
    return a^1

def flip(A):
    A = map(xor,A)
    print A
    for i in xrange(1,len(A)):
        A[i] = A[i-1]+ (1 if A[i]==1 else 0)
    
    print A

A = [0,0,1,1,1,0]
print flip(A)
