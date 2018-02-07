def powerRemainder02(A,B,C):
    x,n,d = A,B,C
    if d==0:
        return -1
    if x==0:
        return 0

    x = x%d
    if x < abs(d-x):
        sign = True
    else:
        sign = False if n%2!=0 else True
        x = abs(d-x)

    mult = 1
    cycle = 1

    cycleLookup = {}
    cycleSet = set()

    #print x,abs(d-x)
    while (mult*x)%d not in cycleSet:
        mult = (mult*x)%d
        cycleSet.add(mult)
        cycleLookup[cycle]=mult

        cycle = cycle+1

    #print cycle
    val = 2 if n/cycle > 1 else 1
    #print val,cycle

    cycle -= val
    cycleLookup[0]=cycleLookup[cycle]
    #print cycle
    #print x,cycle,cycleLookup
    #print cycleSet

    n = n%cycle

    return cycleLookup[n] if sign==True else d-cycleLookup[n]

def powerRemainder(x,n,d):
    ans = 1
    square = x
    if n==0:
        return 1

    while n:
        if n%2:
            ans = ans*square

        square = (square*square)%d
        n = n/2
        if ans > d:
            ans = ans%d

    return ans

#print powerRemainder(9999999,100,99)
#print powerRemainder(2,3,3)
#print powerRemainder(1,1,0)
#print powerRemainder(0,0,1)
#print powerRemainder(10,10,14)
print powerRemainder(71045970,41535484,64735492)
#print powerRemainder(3,8,5)
#print powerRemainder(1878784,45678,451245)
