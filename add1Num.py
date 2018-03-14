#https://www.interviewbit.com/problems/add-one-to-number/

def plusOne(A):
    carry = 1
    for i in xrange(len(A)-1,-1,-1):
        A[i] += carry
        carry = A[i]/10
        A[i] %= 10
    if carry>0:
        A.insert(0,carry)
    while A[0] == 0:
        A.pop(0)
    return A

A = [1,2,3]
print plusOne(A)
