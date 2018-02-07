def primeSum02(A):
    if A%2!=0:
        return

    i = 2
    while i <= A/2:
        if prime02(i) and prime02(A-i):
            return i,A-i
	i += 1
    return

def prime02(x):
    if x<2:
        return False

    if x==2:
        return True

    if x%2==0:
        return False

    p = 3
    while p*p <= x:
        if x%p==0:
            return False
        p += 2
    return True

def primeSum(A):
	if A%2!=0:
		return

	lookup = [2]
	
	i = 3
	while i<A:
		if prime(i,lookup):
			lookup.append(i)
		i += 2

	print lookup
	new_lookup = set(lookup)
	
	for i in lookup:
		if A-i in new_lookup:
			return i,A-i
	return 

def prime(x,lookup):
	sqrt = int(x**(0.5))
	i,temp = 0,lookup
	n = len(temp)
	while i < n and temp[i] <= sqrt:
		if x%temp[i]==0:
			return False
		i += 1
	return True

def primeSieve(N):
	prime = [True for i in range(N+1)]

	p = 2
	while p*p <= N:
		if prime[p]==True:
			#Update all multiples of p, starting from 2nd multiple
			for i in range(p*2,N+1,p):
				prime[i] = False

		p += 1
	
	if prime[2]==True and prime[N-2]==True:
		return 2,N-2

	for p in xrange(3,N,2):
		if prime[p]==True and prime[N-p]==True:
			return p,N-p
	return


"""
print primeSum(16)
#print primeSum(10**10+16)
print primeSum(378)
print primeSum(4)
print primeSum(1000)
#print primeSum(1048574)
#print primeSum(16777214)
print primeSieve(10)
print primeSieve(16777214)
"""
print primeSum02(16777214)
print primeSum02(378)
print primeSum02(4)
print primeSum02(12)
