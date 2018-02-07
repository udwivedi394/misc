import time

INF = 10**8
def allocateBooks(A,B):
    n = len(A)
    start = 0
    end = sum(A)

    mini = INF
    while start < end:
        mid = (start+end)/2
        time.sleep(0.2)
        students = findMaxStudents(A,mid)
        print "Iteration:",(start,end),mid,students
        #if students == B:
        #    mini = min(mini,V)
        if students <= B:
            mini = min(mini,mid)
            end = mid-1
        else:
            start = mid+1
    return mini

def findMaxStudents(A,V):
    students = 1
    sumi = 0
    for i in range(len(A)):
        if A[i] > V:
            return INF

        if sumi+A[i] > V:
            print "Here:",A[i]
            students += 1
            sumi = A[i]
        else:
            sumi += A[i]
        #print
    #if sumi <= V:
    #    students += 1
    return students

A = [100,12,34,67,90,115,11]
#print allocateBooks(A,3)
print findMaxStudents(A,214)


B = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
#print allocateBooks(B,5)
