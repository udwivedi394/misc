def lcs02(A,B):
    n,m = len(A),len(B)
    lookup = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1]==B[j-1]:
                lookup[i][j] = lookup[i-1][j-1]+1
            else:
                lookup[i][j] = max(lookup[i-1][j],lookup[i][j-1])
    return lookup[n][m]

def lcs(A,B):
    n,m = len(A),len(B)
    lookup = [[0 for i in range(m+1)] for j in range(2)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1]==B[j-1]:
                lookup[1][j] = lookup[0][j-1]+1
            else:
                lookup[1][j] = max(lookup[0][j],lookup[1][j-1])
        #print lookup
        lookup[0] = lookup[1]
        lookup[1] = [0 for i in range(m+1)]
    return lookup[0][m]

A = "MZJAWXU"
B = "XMJYAUZ"

#print lcs(A,B)

A = "UTKARSH"
B = "SHWETA"

#print lcs(A,B)

A = "banana"
#print lcs(A,A[::-1])

A = "aaaabaaa"
print lcs(A,A[::-1])

A = "abacdfgdcaba"
print lcs(A,A[::-1])
