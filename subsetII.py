#https://www.interviewbit.com/problems/subsets-ii/
import time
"""
def subsetII(A):
    n = len(A)
    B = 2**n
    final_arr = set()
    for ctr in xrange(B):
        temp = ""
        for i in xrange(n):
            if (ctr>>i)&1!=0:
                temp += "%d|"%(A[i])
        if temp not in final_arr:
            final_arr.add(temp)
    #print final_arr
    result = [map(int,final_arr.pop().split('|')[:-1]) for i in xrange(len(final_arr))]
    return sorted(result)

"""
def subsetsWithDup(A):
    A.sort()
    final_arr = []
    subsetWithDupUtility(A,0,[],final_arr)
    return sorted(final_arr)

def subsetWithDupUtility(A,index,stri,final_arr):
    if index>=len(A):
        final_arr.append(stri)
        return

    subsetWithDupUtility(A,index+1,stri+[A[index]],final_arr)
    temp = index
    while temp < len(A) and A[temp]==A[index]:
        temp+=1
    subsetWithDupUtility(A,temp,stri,final_arr)
    return

A = [1,2,2]
#print subsetsWithDup(A)

A = [ 6, 6, 3, 3, 6, 5 ]
print subsetsWithDup(A)
