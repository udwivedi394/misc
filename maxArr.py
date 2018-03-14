#https://www.interviewbit.com/problems/maximum-absolute-difference/

def maxArr02(A):
    sumi = 0
    for i in xrange(len(A)):
        for j in xrange(i+1,len(A)):
            print (i,j),
            sumi = max(sumi,abs(A[i]-A[j])+abs(i-j))
    return sumi

def maxArr(A):
    INF = 10**10
    mini1,mini2 = INF,INF
    maxi1,maxi2 = -INF,-INF
    for i in xrange(len(A)):
        mini1 = min(mini1, A[i]+i)
        maxi1 = max(maxi1, A[i]+i)
        mini2 = min(mini2, A[i]-i)
        maxi2 = max(maxi2, A[i]-i)

    print mini1, maxi1, mini2,maxi2
    #return maxi-mini

A = [1,3,-1]
A = [ -98, -5, 37, -97, 38, 22, 70, 42, 61, 84 ]
print maxArr(A)
