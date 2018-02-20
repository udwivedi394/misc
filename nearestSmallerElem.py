#https://www.interviewbit.com/problems/nearest-smaller-element/

INF = 10**10
def nearestSmallerElem(A):
    stack = []
    top = -1
    G = []

    for val in A:
        while top >= 0 and stack[top] >= val:
            stack.pop()
            top -= 1
        if top == -1:
            G.append(-1)
        else:
            G.append(stack[top])
        stack.append(val)
        top += 1
    return G

def nearestSmallerElem03(A):
    queue = [A[0]]
    G = [-1]
    front = 0
    top = 0
    for i in xrange(1,len(A)):
        while front < len(queue) and A[i] < queue[front]:
            front += 1
        if front <= top:
            temp = top
            while temp >= front and queue[temp] >= A[i]:
                temp -= 1
            if temp >= front:
                G.append(queue[temp])
            else:
                G.append(-1)
        else:
            G.append(-1)
        queue.append(A[i])
        top += 1
    return G

def nearestSmallerElem02(A):
    mini = INF
    stack = []
    for i in xrange(len(A)):
        j = i-1
        while j >= 0 and A[j]>=A[i]:
            j -= 1
        if j >= 0 and A[j] < A[i]:
            stack.append(A[j])
        else:
            stack.append(-1)
    return stack


A = [4, 5, 2, 10, 8]
#print nearestSmallerElem(A)

A = [3, 2, 1]
#print nearestSmallerElem(A)

A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
#print A
#print nearestSmallerElem(A)

A = [ 39, 27, 11, 4, 24, 32, 32, 1 ]
#print A
#print nearestSmallerElem(A)

A = [ 8, 23, 22, 16, 22, 7, 7, 27, 35, 27, 32, 20, 5, 1, 35, 28, 20, 6, 16, 26, 48, 34 ]
print A
print nearestSmallerElem(A)
