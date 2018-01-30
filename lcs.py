maxofarr = lambda x,y: x if len(x) > len(y) else y

#Dynamic Programming, (Memoization top to bottom approach)
def findLCS_02(str1, str2, edistDir = None):
    
        #If len of one of the string is zero, then no common substring, return blank
        if len(str1) == 0 or len(str2) == 0:
                return ''
   	
	flag = False 
        #Create a new directory if not present
        if edistDir == None:
		flag = True
                edistDir = {}

        #If subsolution of (str1, str2) present in lookup table then return the value
        if edistDir.get((str1, str2))!=None:
                return edistDir.get((str1, str2))

        #if last character of both string same then, call recursively for prefixes of str1, str2 and concatenate current character in it
        if str1[-1] == str2[-1]:
                return findLCS_02(str1[:-1], str2[:-1], edistDir) + str1[-1]

        #lookup in (a, bY)
        arr1 = findLCS_02(str1[:-1], str2, edistDir)
        #lookup in (aX, b)
        arr2 = findLCS_02(str1, str2[:-1], edistDir)

        #Save result in lookup table
        edistDir[(str1, str2)] = maxofarr(arr1, arr2)
	
	if flag:
		print edistDir

        return edistDir[(str1, str2)]
#Solution provided on GeeksforGeeks, it just returns the length of LCS
def findLCS_04(X, Y): 
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 : 
                L[i][j] = 0 
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

#Solution provided on GeeksforGeeks, it just returns the length of LCS
def findLCS_05(X, Y): 
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    #L = [[None]*(n+1) for i in xrange(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    L = [[0]*(n+1) for i in xrange(2)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                L[1][j] = L[0][j-1]+1
            else:
                L[1][j] = max(L[0][j] , L[1][j-1])
	L[0] = L[1]
	L[1] = [0]*(n+1) 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    #print L
    return L[0][-1]

s1 = raw_input().strip()
s2 = raw_input().strip()
#result = commonChild(s1, s2)
result = findLCS_05(s1, s2)
print(result)
