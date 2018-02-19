#https://www.interviewbit.com/problems/largest-rectangle-in-histogram/
class Stack:
    def __init__(self):
        self.data = []
        self.topi = -1

    def push(self,data):
        self.data.append(data)
        self.topi += 1

    def pop(self):
        if self.topi >= 0:
            temp = self.data.pop()
            self.topi -= 1
            return temp
        else:
            return False

    def top(self):
        return self.data[self.topi]

    def empty(self):
        if self.topi >= 0:
            return False
        else:
            return True

    def __str__(self):
        return ("Stack:%s")%self.data

def findMaxAreaStack(arr):
    s = Stack()

    max_area = -1
    area_with_top = -1
    i = 0 
    n = len(arr)

    #Traverse through histogram
    while i < n:
        #If stack is empty or the arr[top of stack] <= arr[i](current bar in histogram), push current bar index, increment i
        #This way stack will always be in increasing order of bars
        if s.empty() or arr[s.top()] <= arr[i]:
            s.push(i)
            i += 1
            print "Inside if Stack:",s
        #If current element is lesser than arr[top of stack]
        else:
            #save index of top bar
            tp = s.top()
            #Pop the stack
            s.pop()
    
            #Multiply the current bar with all bars in right side, as the bars in right will be always greater than current bar
            #Taking the new top is important, as if there was a bigger bar between top bar and the previous one,
            #It should also be multiplied with current top bar area
            area_with_top = arr[tp] * (i if s.empty() else i-s.top()-1)
            max_area = max(max_area, area_with_top)
            print "Inside else stack:",s

    while s.empty()==False:
        tp = s.top()
        s.pop()

        print "Outer Stack:",s
        area_with_top = arr[tp] * (i if s.empty() else i-s.top()-1)
        max_area = max(max_area, area_with_top)

    return max_area

A = [2,1,5,6,2,3]
print findMaxAreaStack(A)
