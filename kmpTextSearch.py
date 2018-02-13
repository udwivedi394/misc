def minPalindrome(A):
    B = A+'$'+A[::-1]

    lookup = patternSearch("",B,True)
    print lookup
    return len(A)-lookup[-1]

def patternSearch(A,B=None,lpsArr=False):
    lookupB = [0]*len(B)

    j,i = 0,1
    while i < len(B):
        if B[j] == B[i]:
            lookupB[i] = j+1
            j += 1
        else:
            if j > 0:
                j = lookupB[j-1]
                continue
        i += 1

    if lpsArr:
        return lookupB
    
    i = 0 #counter for original text
    j = 0 #counter for lookupB

    foundIndex = []
    while i < len(A):
        if A[i] == B[j]:
            j += 1
            if j >= len(B):
                foundIndex.append(i-j+1)
                j = 0
        else:
            if j > 0:
                j = lookupB[j-1]
                continue
        i += 1
    return foundIndex

B = "abcdabca"
#print patternSearch("",B)

B = "aabaabaaa"
#print patternSearch("",B)

B = "abcaby"
A = "abxabcabcabyxabcaby"
#print patternSearch(A,B)

A = "ABABDABACDABABCABAB"
B = "ABABCABAB"
#print patternSearch(A,B)

#print minPalindrome("UTKARSH")
#print minPalindrome("ABC")

A = "aaaabaaa"
print patternSearch("",A+'$'+A[::-1],True)
