#https://www.interviewbit.com/problems/subset/

def subset(A):
    A.sort()
    B = 2**len(A)
    final_arr = []
    for ctr in xrange(B):
        temp = []
        for i in xrange(len(A)):
            if (ctr>>i)&1!=0:
                temp.append(A[i])
        final_arr.append(temp)
    return sorted(final_arr)

A = [1,2,3,4]
print subset(A)
