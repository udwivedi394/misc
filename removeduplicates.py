#https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(A):
    n = len(A)
    if n in (0,1):
        return n

    backctr = 0
    frontctr = 1

    count = 1

    while frontctr < n:
        if A[frontctr]==A[backctr]:
            frontctr += 1
        else:
            swap(A,frontctr,backctr+1)
            frontctr += 1
            backctr += 1
            count += 1
    #print A
    return count

def swap(A,x,y):
    if x==y:
        return
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    return


def removeDuplicates02(A):
    n = len(A)
    if n in (0,1):
        return n

    backctr = 0
    frontctr = 1

    while frontctr < n:
        if A[frontctr]==A[backctr]:
            A.pop(frontctr)
            n -= 1
        else:
            backctr += 1
            frontctr += 1
    print A
    return n

A = [1,2,2,2,3]
print removeDuplicates(A)
