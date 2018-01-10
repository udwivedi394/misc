def coinChange(arr,n,k):
	if k==0:
		return 1
	
	if n<0 or k<0:
		return 0

	return coinChange(arr,n,k-arr[n])+coinChange(arr,n-1,k)


def coinChange02(arr,n,k,lookup={}):
	if k==0:
		return 1
	
	if n<0 or k<0:
		return 0
	
	if lookup.get(n*1000+(k-arr[n]))==None:
		lookup[n*1000+(k-arr[n])] = coinChange02(arr,n,k-arr[n],lookup)

	if lookup.get((n-1)*1000+k)==None:
		lookup[(n-1)*1000+k] = coinChange02(arr,n-1,k,lookup)

	return lookup[n*1000+(k-arr[n])]+lookup[(n-1)*1000+k]

arr = [2,5,3,6]
arr2 = [1,2,3]
print coinChange02(arr,len(arr)-1,10)
