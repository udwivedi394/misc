#https://www.interviewbit.com/problems/combination-sum-ii/

def combSumII(A,B):
    A.sort()
    print A
    final_result = []
    combSumIIUtil(A,0,B,[],final_result)
    #combSumIIUtil(A,B,[],final_result)
    return final_result

def combSumIIUtil(A,cur_sum,target,stri,final_result):
    #print "A:",A,"cur_sum:",cur_sum,"target:",target,"stri:",stri,"final_result:",final_result
    if len(A)==0:
        if cur_sum==target:
            final_result.append(stri)
        return

    if cur_sum+A[0] <= target:
        combSumIIUtil(A[1:],cur_sum+A[0],target,stri+[A[0]],final_result)
        low=temp=0
        while temp < len(A) and A[temp] == A[low]:
            temp += 1
        combSumIIUtil(A[temp:],cur_sum,target,stri,final_result)
    else:
        low=temp= 0
        while temp < len(A) and A[temp] == A[low]:
            temp += 1
        combSumIIUtil(A[temp:],cur_sum,target,stri,final_result) 
    return

A = [10,1,2,7,6,1,5]
B = 8

A = [1, 1,2, 5, 6, 7, 10]
#print combSumII(A,B)

A = [ 8, 10, 6, 11, 1, 16, 8 ]
B = 28

A = [1, 6, 8, 8, 10, 11, 16]
#print combSumII(A,B)

A = [ 17, 8, 17, 20, 20, 18, 14, 15, 20, 3 ]
B = 14

A = [3, 8, 14, 15, 17, 17, 18, 20, 20, 20]
#print combSumII(A,B)

A = [ 15, 8, 15, 10, 19, 18, 10, 3, 11, 7, 17 ]
B = 33
#print combSumII(A,B)

A = [2,3,6,7]
B = 7
print combSumII(A,B)
