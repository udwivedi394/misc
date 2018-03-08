#https://www.interviewbit.com/problems/colorful-number/
from collections import defaultdict

def colorful(A):
    lookup = defaultdict(int)
    
    A = map(int,list(str(A)))
    count = 0
    for i in xrange(len(A)):
        j = i
        mult = 1
        while j < len(A):# and j-i < len(A)-1:
            mult *= A[j]
            lookup[mult] += 1
            count += 1
            j += 1
    print lookup, count
    if count == len(lookup):
        return True
    return False

print colorful(3245)
