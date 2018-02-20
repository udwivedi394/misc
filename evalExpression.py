#https://www.interviewbit.com/problems/evaluate-expression/

def evalExpr(A):
    stack = []
    for i in A:
        if i == '+':
            stack.append(stack.pop()+stack.pop())
        elif i == '-':
            stack.append(-stack.pop()+stack.pop())
        elif i == '*':
            stack.append(stack.pop()*stack.pop())
        elif i == '/':
            temp = stack.pop()
            stack.append(stack.pop()/temp)
        else:
            stack.append(int(i))
    return stack[0]

A = ["2", "1", "+", "3", "*"]
print evalExpr(A)

A = ["4", "13", "5", "/", "+"]
print evalExpr(A)
