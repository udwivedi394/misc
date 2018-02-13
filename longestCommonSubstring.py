def lcsubstring(A):
    B = A[::-1]
    n = len(A)
    lookup = [[0 for i in range(n+1)] for j in range(2)]

    maxi = [0,0]
    #keeping reverse string on vertical axis
    for i in range(1,n+1):
        for j in range(1,n+1):
            if B[i-1] == A[j-1]:
                lookup[1][j] = lookup[0][j-1]+1
                if lookup[1][j] >= maxi[0]:
                    res = A[j-lookup[1][j]:j]
                    if res == res[::-1]:
                        maxi = lookup[1][j],j
        lookup[0] = lookup[1]
        lookup[1] = [0]*(n+1)

    res = A[maxi[1]-maxi[0]:maxi[1]]
    print res
    if res == res[::-1]:
        return res
    return lcsubstring(res)


def lcsubstring03(A):
    B = A[::-1]
    n = len(A)
    lookup = [[0 for i in range(n+1)] for j in range(2)]

    maxi = [0,0]
    #keeping reverse string on vertical axis
    for i in range(1,n+1):
        for j in range(1,n+1):
            if B[i-1] == A[j-1]:
                lookup[1][j] = lookup[0][j-1]+1
                if lookup[1][j] >= maxi[0]:
                    res = A[j-lookup[1][j]:j]
                    if res == res[::-1]:
                        maxi = lookup[1][j],j
        lookup[0] = lookup[1]
        lookup[1] = [0]*(n+1)

    res = A[maxi[1]-maxi[0]:maxi[1]]
    print res
    if res == res[::-1]:
        return res
    return lcsubstring(res)

def lcsubstring02(A):
    B = A[::-1]
    n = len(A)
    lookup = [[0 for i in range(n+1)] for j in range(n+1)]

    maxi = [0,0]
    #keeping reverse string on vertical axis
    for i in range(1,n+1):
        for j in range(1,n+1):
            if B[i-1] == A[j-1]:
                lookup[i][j] = lookup[i-1][j-1]+1
                if lookup[i][j] >= maxi[0]:
                    maxi = lookup[i][j],j

    for i in range(n+1):
        print lookup[i]

    res = A[maxi[1]-maxi[0]:maxi[1]]
    if res == res[::-1]:
        return res
    return lcsubstring(res)

A = "abacdfgdcaba"
print lcsubstring(A)

A = "aaaabaaa"
#print lcsubstring(A)

A = "abbcccbbbcaaccbababcbcabca"
#print lcsubstring(A)

A = "caccbcbaabacabaccacaaccaccaaccbbcbcbbaacabccbcccbbacbbacbccaccaacaccbbcc"
#print lcsubstring(A)
