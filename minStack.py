#https://www.interviewbit.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = [[10**10,1]]
        self.mini = 10**10

    def push(self,x):
        self.stack.append(x)
        if x < self.mini:
            #self.minstack.append(self.mini,1)
            self.minstack.append([x,1])
            self.mini = x
        elif x == self.mini:
            self.minstack[-1][1] += 1
    
    def pop(self):
        if self.minstack[-1][0]==self.top():
            if self.minstack[-1][1] == 1:
                self.minstack.pop()
                self.mini = self.minstack[-1][0]
            else:
                self.minstack[-1][1] -= 1

        if self.stack:
            return self.stack.pop()
        return

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1
    
    def getMin(self):
        if len(self.stack)==0:
            return -1

        if self.minstack[-1][0]==10**10:
            return -1

        return self.minstack[-1][0]

stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
#print stack.top()
#print stack.getMin()
#print stack.pop()
#print stack.getMin()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print stack.getMin()
print stack.stack
print stack.minstack
