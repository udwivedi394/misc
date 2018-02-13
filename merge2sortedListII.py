def merge(A,B):
    ctr1 = ctr2 = 0
    n,m = len(A),len(B)

    while ctr1 < n and ctr2 < m:
        print "ctr1:",ctr1,A,"ctr2:",ctr2,B
        if A[ctr1] < B[ctr2]:
            ctr1 += 1
        elif A[ctr1] >= B[ctr2]:
            A.insert(ctr1,B[ctr2])
            ctr1 += 1
            ctr2 += 1
            n += 1
    while ctr2 < m:
        A.append(B[ctr2])
        ctr2 += 1
    return A

A = [1,5,8]
B = [6,9]

#print merge(A,B)

A = [3]
B = [-4,-3]
print merge(A,B)
