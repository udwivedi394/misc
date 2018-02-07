def unknownPivotsearch(A):
    start = 0
    end = len(A)-1

    while start <= end:
        mid = (start+end)/2

        if mid+1 <= end and A[mid+1] < A[mid]:
            #print "Pivot found:",mid
            return mid
        
        if mid-1 >= start and A[mid-1] > A[mid]:
            #print "Pivot found:",mid-1
            return mid-1

        if A[start] > A[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1

def binarySearchRotated(A,k):
    pivot = unknownPivotsearch(A)

    start = 0
    end = len(A)-1

    if pivot != -1:
        if k >= A[0]:
            end = pivot
        else:
            start = pivot+1

    print "start,end:",(start,end)
    while start <= end:
        mid = (start+end)/2
        
        if k == A[mid]:
            return mid
        
        if k < A[mid]:
            end = mid-1
    
        if k > A[mid]:
            start = mid+1

    return -1

A = [0,1,2,3,4,5,6,7,8]
print unknownPivotsearch(A)

B = [5,6,7,8,9,0,1,2,3,4]
print unknownPivotsearch(B)

C = [3,4,5,6,7,8,0,1,2]
print unknownPivotsearch(C)

print binarySearchRotated(C,8)

D = [0]
print binarySearchRotated(D,2)
