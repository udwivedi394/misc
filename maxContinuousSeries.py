#https://www.interviewbit.com/problems/max-continuous-series-of-1s/
INF = 10**10
def maxContinuous(A,k):
    n = len(A)
    #Store the indexes of all the 0s from the original array start with -1
    zeroes = [-1]
    for i in xrange(n):
        if A[i]==0:
            zeroes.append(i)
    #Ending with Len(A)
    zeroes.append(n)

    ctr1 = result = start = end = 0
    ctr2 = min(len(zeroes)-1,ctr1+k+1)
    while ctr2 < len(zeroes):
        temp = zeroes[ctr2]-zeroes[ctr1]-1
        if temp > result:
            result = temp
            start = zeroes[ctr1]+1
            end = start+result
        ctr1 += 1
        ctr2 = ctr1+k+1
    
    return list(range(start,end))
        

def maxContinuous02(A,k):
    n = len(A)
    result = 0
    end_index = -INF
    for i in xrange(1,n):
        if A[i]==1:
            A[i] = A[i-1]+1
        if A[i] > result:
            result = A[i]
            end_index = i+1
    print end_index,result

    ctr1 = 0
    while ctr1 < n:
        if A[ctr1]==0:
            rem = k
            count = A[ctr1-1] if ctr1>0 else 0
            ctr2 = ctr1
            while ctr2 < n and rem>=0:
                if A[ctr2]==0:
                    if rem > 0:
                        rem -= 1
                    else:
                        break
                count += 1
                ctr2 += 1
            
            if count > result:
                result = count
                end_index = ctr2

        ctr1 += 1

    print A,result
    return list(xrange(end_index-result,end_index))

A = [1,0,1,1,0,1,0,1,1,1,0,0]
#print maxContinuous(A,3)

A = [0,1,1,1]
#print maxContinuous(A,0)

A = [1,1,0]
#print maxContinuous(A,2)
