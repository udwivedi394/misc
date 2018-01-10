def makeSum(arr,k):
	count = [0]
	n = len(arr)
	lookup = {}
	makeSumUtility(arr,0,k,0,count,n,lookup)
	#print lookup
	return count[0]

def isSafe(arr,index,cur_sum,k,n):
	if index>=n:
		return False
	if cur_sum+arr[index] > k:
		return False
	return True

def makeSumUtility(arr,index,k,cur_sum,count,n,lookup):
	if cur_sum > k or index >= n:
		return 0
	
	if lookup.get(index*100+(k-cur_sum))==None:
		lookup[index*100+(k-cur_sum)] = -1
	else:
		if lookup[index*100+(k-cur_sum)]==1:
			count[0] += 1
			return 1
		elif lookup[index*100+(k-cur_sum)]==0:
			return 0	
	if cur_sum == k:
		count[0] += 1
		lookup[index*100+(k-cur_sum)] = 1
		return 1
	"""	
	val = lookup[index*100+(k-cur_sum)]
	key = index*100+(k-cur_sum)
	print "index:%d,sum_to_make:%d,count:%d,key:%d,lookup:%s"%(index,k-cur_sum,count[0],key,str(val))
	"""
	if arr[index] > (k-cur_sum):
		lookup[index*100+(k-cur_sum)] = 0

	if isSafe(arr,index,cur_sum,k,n):
		val1 = makeSumUtility(arr,index,k,cur_sum+arr[index],count,n,lookup)
		if val1 == 1:
			lookup[index*100+(k-(cur_sum+arr[index]))] = 1
		
		val2 = makeSumUtility(arr,index+1,k,cur_sum,count,n,lookup)
		if val2 == 1:
			lookup[(index+1)*100+(k-(cur_sum))] = 1
	else:	
		val3 = makeSumUtility(arr,index+1,k,cur_sum,count,n,lookup)
		if val3 == 1:
			lookup[(index+1)*100+(k-(cur_sum))] = 1	
	return 0

def makeSum02(arr,k):
	n = len(arr)
	count = [0]
	lookup = {}
	for i in range(n):
		if k%arr[i]==0:
			lookup[i*100+k] = True
	
	makeSumUtility02(arr,0,k,k,lookup,count,n)
	return count[0]

def makeSumUtility02(arr,index,k,cur_sum,lookup,count,n):
	if cur_sum > k or index >= n:
		return

	if cur_sum == 0:
		count[0] += 1

	if lookup[index*100+cur_sum]:
		pass

arr = [2,5,3,6]
arr2 = [1,2,3]
print makeSum(arr,10)
print makeSum(arr2,4)
print makeSum(arr2,0)
print makeSum([],10)
