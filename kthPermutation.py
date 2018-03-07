#https://www.interviewbit.com/problems/kth-permutation-sequence/

def getPermutation(A,B):
    num = ""
    mainList = [i for i in xrange(1,A+1)]
    B -= 1
    i = 1
    while mainList:
        curFact = factorial(A-i)
        temp1 = mainList.pop(B//curFact)
        num += str(temp1)
        B = B%curFact
        i += 1
    return num

def factorial(n):
    mult = 1
    for i in xrange(1,n+1):
        mult *= i
    return mult

print getPermutation(10,101)
