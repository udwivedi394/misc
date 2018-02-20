#https://www.interviewbit.com/problems/sliding-window-maximum/

def slidingWindowMax(A,B):
    stack = [0]
    i,n = 1,len(A)
    while i < n and i < B:
        while stack and A[stack[-1]] < A[i]:
            stack.pop()
        stack.append(i)
        i += 1

    front = 0           #pointer to lower end of stack
    lower = 0           #counter to track the lower end of window
    B = [A[stack[front]]]
    try:
        while i < n:
            while len(stack)>front and A[stack[-1]] < A[i]:
                stack.pop()
            stack.append(i)
    
            if lower >= stack[front]:
                front += 1

            B.append(A[stack[front]])
            lower += 1
            i += 1
        return B
    except Exception as e:
        print e

A = [1,3,-1,-3,5,3,6,7]
#print slidingWindowMax(A,3)

A = [1,3,-1,-3,-5,3,6,7]
print A
print slidingWindowMax(A,3)
