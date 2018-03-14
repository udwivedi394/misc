#QuickSort

def partition(A,low,high):
    i,j = low-1,low
    pivot = high-1

    while j < high:
        if A[j] < A[pivot]:
            i += 1
            A[i],A[j] = A[j],A[i]
        j += 1

    A[i+1],A[pivot] = A[pivot],A[i+1]
    return i+1

def quicksort(A,low=0,high=None):
    if high==None:
        high = len(A)
    if low < high:
        p = partition(A,low,high)
        quicksort(A,low,p-1)
        quicksort(A,p+1,high)
    return

A = [10, 80, 30, 90, 40, 50, 70]
quicksort(A)
print A
