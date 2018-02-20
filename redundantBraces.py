#https://www.interviewbit.com/problems/redundant-braces/

#Return 1 if redundant Braces are present
def redundantBraces(A):
    stack = []

    for i in A:
        if i == ')':
            valid = False
            while stack[-1] != '(':
                if stack.pop() in ('+','*','-','/'):
                    valid = True
            if valid==False:
                return 1
            stack.pop()
        elif i in ('(','+','*','-','/'):
            stack.append(i)
    return 0

A = "((a + b))"
print redundantBraces(A)


A = "(a + (a + b))"
print redundantBraces(A)
