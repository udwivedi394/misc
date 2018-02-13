#https://www.interviewbit.com/problems/3-sum/

INF = 10**10
def threesum(A,B):
    A.sort()
    mini = final = INF
    for i in xrange(len(A)):
        temp = twosum(A[i:],B-A[i])
        if abs(B-(temp+A[i])) < mini:
            final = temp+A[i]
            mini = abs(B-(temp+A[i]))
    return final

def threesum03(A,B):
    A.sort()
    print A
    mini = INF
    final = INF
    for i in xrange(len(A)):
        temp_arr = []+A
        temp_arr.pop(i)
        temp = twosum(temp_arr,B-A[i])
        print "B:",B,"mini:",mini,"i:",A[i],"B-A[i]:",B-A[i],temp
        if abs(B-(temp[0]+A[i])) < mini:
            final = temp[0]+A[i]
            mini = abs(B-(temp[0]+A[i]))
    return final

def threesum02(A,B):
    A.sort()
    print A
    mini,select= twosum(A,B)
    print mini,select
    temp = new = INF
    A[select[0]] = INF
    A[select[1]] = INF

    for i in A:
        print "B:",B,"mini:",mini,"i:",i,"abs(B-(mini+i)):",abs(B-(mini+i))
        if abs(B-(mini+i)) < temp:
            temp = abs(B-(mini+i))
            new = mini+i 
    return new

def twosum(A,k):
    low = 0
    high = len(A)-1
    mini = INF
    while low < high:
        if abs(k-(A[low]+A[high])) < abs(k-mini):
            mini = A[low]+A[high]
        if A[low]+A[high]==k:
            return k
        elif A[low]+A[high] < k:
            low += 1
        elif A[low]+A[high] > k:
            high -= 1
    return mini

def twosum02(A,k):
    #print A
    low = 0
    high = len(A)-1
    mini = 10**10
    select = []
    while low < high:
        #print mini
        if abs(k-(A[low]+A[high])) < abs(k-mini):
            mini = A[low]+A[high]
            select = [low,high]
        if A[low]+A[high]==k:
            return k,select
        elif A[low]+A[high] < k:
            low += 1
        elif A[low]+A[high] > k:
            high -= 1
    #print "Here"
    return mini,select

A = [-1,2,1,-4]
#A = [-4,-1,1,2]
#print twosum(sorted(A),4)
#print threesum(A,1)

A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
B = -3


#print threesum(A,B)
#temp = sorted(A)
#print temp
#mini,select = twosum(temp[1:],5)
#print mini, temp[1+select[0]],temp[1+select[1]]

A = [ -10, -10, -10 ]
B = -5
print threesum(A,B)
#print twosum(A,-5)
