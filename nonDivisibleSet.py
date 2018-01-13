def nonDivisibleSubset(k,arr):
	freq = [0]*k
	for i in arr:
		freq[i%k]+=1

	if (k%2==0):
		freq[k/2]=min(freq[k/2],1)

	res = min(freq[0],1)
	for i in range(1,k/2+1):
		res += max(freq[i],freq[k-i])
	
	return res

arr = [2,7,1,4]
print nonDivisibleSubset(3,arr)
