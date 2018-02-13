INF = 10**7
def lengthofLastWord02(A):
    start = -1
    end = -1

    i = 0
    n = len(A)
    while i < n:
        if A[i]==' ':
            if end == INF:
                end = i-1
        else:
            if end != INF:
                start = i
                end = INF
        i += 1
    print start,end,# A[start],A[end]
    if start < 0:
        return 0
    if A[i-1]!=' ':
        end = len(A)-1
    return end-start+1


def lengthofLastWord(A):
    length = 0
    current = False

    i = 0
    n = len(A)
    while i < n:
        if A[i]==' ':
            if length:
                current = False
        else:
            if current==False:
                length = 1
                current = True
            else:
                length += 1
        i += 1
    return length

#A = "hello world"
#A = ""

A = "    hello     world  Utkarsh   "
print lengthofLastWord(A)

