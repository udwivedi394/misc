#https://www.interviewbit.com/problems/repeat-and-missing-number-array/

def repeatedNumber(A):
    n = len(A)
    
    sumi = sq_sumi = 0
    cur_sumi = cur_sq_sumi = 0
    for i in xrange(1,n+1):
        sumi += i
        sq_sumi += i**2
        cur_sumi += A[i-1]
        cur_sq_sumi += A[i-1]**2

    d = sumi-cur_sumi
    c = sq_sumi-cur_sq_sumi

    #print d,c
    A = (c-d**2)/(2*d)
    B = d+A
    return [A,B]
        

A = [3,1,2,5,3]
print repeatedNumber(A)
