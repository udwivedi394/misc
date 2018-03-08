#https://www.interviewbit.com/problems/permutations/

def permute(A):
    final_arr = []
    permuteUtil(sorted(A),[],final_arr)
    return final_arr

def permuteUtil(A,stri,final_arr):
    #print "A:",A,"stri:",stri,"final_arr:",final_arr
    if len(A)==1:
        final_arr.append(stri+A)
    for i in xrange(len(A)):
        #temp = []+A
        swap(A,0,i)
        #print temp
        permuteUtil(sorted(A[1:]),stri+[A[0]],final_arr)
        swap(A,i,0)
    return

def swap(A,x,y):
    if x==y:
        return
    A[x] = A[x]^A[y]
    A[y] = A[x]^A[y]
    A[x] = A[x]^A[y]

A = [1,2,3,4,5]
print permute(A)
