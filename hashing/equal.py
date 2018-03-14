#https://www.interviewbit.com/problems/equal/

from collections import defaultdict

def equal02(A):
    lookup = defaultdict(list)
    possible_res = set()
    for i in xrange(len(A)):
        for j in xrange(i+1,len(A)):
            sumi = A[i]+A[j]
            lookup[sumi].append((i,j))
            if len(lookup[sumi])>1:
                possible_res.add(sumi)
    print lookup
    print possible_res
    result = []
    for sumi in possible_res:
        for i in xrange(len(lookup[sumi])):
            for j in xrange(i+1,len(lookup[sumi])):
                if lookup[sumi][i][0]<lookup[sumi][j][0] and lookup[sumi][i][1]!=lookup[sumi][j][0] \
                    and lookup[sumi][i][1]!=lookup[sumi][j][1]:
                    result.append((lookup[sumi][i][0],lookup[sumi][i][1],lookup[sumi][j][0],lookup[sumi][j][1]))
    result.sort()
    if result:
        return list(result[0])
    return []

def equal(A):
    lookup = defaultdict(list)
    INF = 10**10
    result = (INF,INF,INF,INF)
    for i in xrange(len(A)):
        for j in xrange(i+1,len(A)):
            sumi = A[i]+A[j]
            found = False
            for k in xrange(len(lookup[sumi])):
                seti = lookup[sumi][k]
                if seti[0]<i and seti[1]!=i \
                    and seti[1]!=j:
                    pass
                else:
                    found = True
            if found==False:
                lookup[sumi].append((i,j))
            lookup[sumi].sort()
            if len(lookup[sumi])>2:
                lookup[sumi].pop()
            if len(lookup[sumi])==2:
                seti = lookup[sumi]
                result = min(result,(seti[0][0],seti[0][1],seti[1][0],seti[1][1]))
    print lookup
    """
    INF = 10**10
    result = (INF,INF,INF,INF)
    for key,seti in lookup.iteritems():
        if len(seti)==2:
            result = min(result,(seti[0][0],seti[0][1],seti[1][0],seti[1][1]))
    print result
    """
    if result!=(INF,INF,INF,INF):
        return list(result)
    return []

A = [3,4,7,1,2,9,8]
print equal(A)

A = [ 0, 0, 1, 0, 2, 1 ]
#print equal(A)
