#https://www.interviewbit.com/problems/sorted-permutation-rank/

def sortedPermRank(A):
    strLookup = sorted(list(A)) 
    n = len(A)
    print strLookup,n
    rank = i = 0
    lookup = []
    while i < n:
        x = strLookup.index(A[i])
        minus = 0
        print "lookup:",lookup,
        for j in lookup:
            if j < x:
                minus += 1
        print "A[i]:",A[i],"Index:",x,"minus:",minus,
        lookup.append(x)
        x -= minus
        y = factorial(n-i-1)
        print "x:",x,"n-i-1:",n-i-1,"y:",y
        rank += x*y
        i += 1
    return (rank+1)%1000003

def factorial(B):
    mult = 1
    while B:
        mult *= B
        B -= 1

    return mult

#print sortedPermRank('Utkarsh')
#print factorial(20)
print sortedPermRank("DTNGJPURFHYEW")
#print factorial(11)
