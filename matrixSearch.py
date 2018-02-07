def matrixSearch(A,k):
    rowL = len(A)
    colL = len(A[0])

    #Row Search
    start = 0
    end = rowL-1

    while start <= end:
        mid = (start+end)/2

        if k >= A[mid][0] and k<=A[mid][-1]:
            break
        elif k < A[mid][0]:
            end = mid-1
        elif k > A[mid][-1]:
            start = mid+1

    row = mid

    start,end = 0,colL-1

    while start <= end:
        mid = (start+end)/2
        
        if k == A[row][mid]:
            return 1

        elif k < A[row][mid]:
            end = mid-1

        elif k > A[row][mid]:
            start = mid+1

    return 0

A = [[1,   3,  5,  7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]

print matrixSearch(A,0)
