def medianSearch02(A,B):
    m,n = len(A),len(B)
    
    next = True
    median = (m+n)/2
    if (m+n)%2!=0:
        next = False

    ctr = -1
    first = None
    for i in xrange(min(A[0],B[0]),max(A[-1],B[-1])+1):
        if binSearch(A,B,i):
            ctr+=1
        if ctr>=median:
            first = i
            if next==False:
                return i
            if next and ctr==median+1:
                return (first+i)/2.0
    return

def binarySearch(A,B,k):
    if A[0]>=k and A[-1]<=k:
        searchArr = A

    elif A[0] >= 1:
        pass

def medianSearch03(A,B):
    m,n = len(A),len(B)

    startA,endA = 0,m-1
    startB,endB = 0,n-1

    while (endA-startA+1)>2 and (endB-startB+1)>2:
        midA = (startA+endA)/2
        midB = (startB+endB)/2

        if A[midA]==B[midB]:
            return A[midA]

        elif A[midA] < B[midB]:
            startA = midA
            endB = midB
        else:
            endA = midA
            startB = midB

    print "startA,startB:",(startA,endA),(startB,endB),"A:",A,"B:",B
    return (max(A[startA],B[startB])+min(A[endB],B[endB]))/2.0

def medianSearch(A,B):
    m,n = len(A),len(B)

    startA,endA = 0,m-1
    startB,endB = 0,n-1

    while (endA-startA+1)>2 and (endB-startB+1)>2:
        midA = (startA+endA)/2
        midB = (startB+endB)/2

        if A[midA]==B[midB]:
            return A[midA]

        elif A[midA] < B[midB]:
            startA = midA
            endB = midB
        else:
            endA = midA
            startB = midB


    print "startA,startB:",(startA,endA),(startB,endB),"A:",A,"B:",B
    return (max(A[startA],B[startB])+min(A[endB],B[endB]))/2.0

B = [1,4]#,70]
#B = [2,3]
A = [99,100,150,200]

print medianSearch(A,B)
