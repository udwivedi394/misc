#https://www.interviewbit.com/problems/single-number/

def singleIntegerI(A):
    xor = 0
    for i in A:
        xor ^= i
    return xor

A = [1,2,2,3,1]
print singleIntegerI(A)
