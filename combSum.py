#https://www.interviewbit.com/problems/combination-sum/
"""
def combSum(A,B):
    A.sort()
    print A
    final_string = []
    combSumUtil(A,B,0,[],final_string)
    return final_string

def combSumUtil(A,B,cur_sum,stri,final_string):
    if len(A)==0:
        if cur_sum == B:
            final_string.append(stri)
        return

    low = temp = 0
    if cur_sum+A[0] <= B:
        combSumUtil(A,B,cur_sum+A[0],stri+[A[0]],final_string)
        while temp<len(A) and A[temp] == A[low]:
            temp += 1
        combSumUtil(A[temp:],B,cur_sum,stri,final_string)
    else:
        while temp<len(A) and A[temp] == A[low]:
            temp += 1
        combSumUtil(A[temp:],B,cur_sum,stri,final_string)
    return

A = [2,3,6,7]
B = 7

#print combSum(A,B)

A = [ 8, 10, 6, 11, 1, 16, 8 ]
B = 28

A = [1, 6, 8, 8, 10, 11, 16]
print combSum(A,B)
"""

def combinationSum(A,B):
    A.sort()
    final_arr = []
    combinationSumUtility(A,0,0,B,[],final_arr)
    return final_arr

def combinationSumUtility(A,index,sumi,target,stri,final_arr):
    if sumi == target:
        final_arr.append(stri)
        return

    if index >= len(A):
        return

    if sumi+A[index] <= target:
        combinationSumUtility(A,index,sumi+A[index],target,stri+[A[index]],final_arr)
        temp = index
        while temp < len(A) and A[temp]==A[index]:
            temp += 1
        combinationSumUtility(A,temp,sumi,target,stri,final_arr)
    return

A = [2,3,6,7]
B = 7
#print combinationSum(A,B)

A = [ 8, 10, 6, 11, 1, 16, 8 ]
B = 28
print combinationSum(A,B)
