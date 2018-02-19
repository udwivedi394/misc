#https://www.interviewbit.com/problems/rain-water-trapped/

def trap(A):
    n = len(A)

    #Store all the heights along with index
    heightStack = [(A[i],i) for i in xrange(n)]
    #Sort the stack according to height
    heightStack.sort()

    ctr1 = 0
    water = 0
    while ctr1 < n:
        #Check that the next height on top of stack lies right of current pointer or not
        while heightStack and heightStack[-1][1] <= ctr1:
            heightStack.pop()

        #print "HeightStack:",heightStack
        if len(heightStack)==0:
            break

        rightMax = heightStack[-1]
        #print "RightMax:",rightMax

        ctr2 = ctr1
        while ctr2 < n and ctr2 < rightMax[1]:
            minHeight = min(rightMax[0],A[ctr1])
            #print "ctr1:",ctr1,"ctr2:",ctr2,"x,y:",(A[ctr1],A[ctr2]),
            if A[ctr2] <= minHeight:
                water += minHeight-A[ctr2]
                ctr2 += 1
            else:
                ctr1 = ctr2
                ctr2 += 1
                
            #print "Water:",water
        ctr1 = ctr2
    return water

A = [0,1,0,2,1,0,1,3,2,1,2,1]
print trap(A)

#print "ctr1:",ctr1,"ctr2:",ctr2,"x,y:",(A[ctr1],A[ctr2]),"Water:",water
