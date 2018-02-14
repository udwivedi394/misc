#https://www.interviewbit.com/problems/counting-triangles/

#Find all possible triangle
def greatersum(A):
    n = len(A)
    if n < 3:
        return 0

    A.sort()
    #Below approach is based on the fact that for A<=B<=C, to be a valid triangle
    #Following condition must be true, A+B > C
    count = 0
    low = 0
    high = n-1
    while high > 1:
        count += sumGreaterthank(A[:high],A[high])
        high -= 1

    return count

#Count the number of pairs with sum greater than k
def sumGreaterthank(A,k):
    low = 0
    high = len(A)-1
    count = 0

    while low < high:
        if A[low]+A[high] > k:
            count += high-low
            high -= 1
        else:
            low += 1
    return count

A = [1,1,1,2,2]
print greatersum(A)
#print sumGreaterthank(A[:2],1)
