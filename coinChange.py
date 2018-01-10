def makeSum(arr,k):
	count = [0]
	n = len(arr)
	lookup = {}
	for i in range(n):
		if k%arr[i]==0:
			lookup[i*100+k] = 1
	print lookup
	makeSumUtility(arr,0,k,0,count,n,lookup)
	print lookup
	return count[0]

def isSafe(arr,index,cur_sum,k,n):
	if index>=n:
		return False
	if cur_sum+arr[index] > k:
		return False
	return True

def makeSumUtility(arr,index,k,cur_sum,count,n,lookup):
	if cur_sum == k:
		count[0] += 1
		return 1
	if cur_sum > k or index >= n:
		return 0
	if lookup.get(index*100+(k-cur_sum))==None:
		lookup[index*100+(k-cur_sum)] = 1 if (k-cur_sum)%arr[index]==0 else -1
	
	else:
		print "Returning from Here"
		if lookup[index*100+(k-cur_sum)]==1:
			count[0] += 1
			return 1
		elif lookup[index*100+(k-cur_sum)]==0:
			return 0
	
	val = lookup[index*100+(k-cur_sum)]
	key = index*100+(k-cur_sum)
	print "index:%d,sum_to_make:%d,count:%d,key:%d,lookup:%s"%(index,k-cur_sum,count[0],key,str(val))

	if isSafe(arr,index,cur_sum,k,n):
		if lookup.get(index*100+(k-(cur_sum+arr[index])))==None:
			lookup[index*100+(k-(cur_sum+arr[index]))]=makeSumUtility(arr,index,k,cur_sum+arr[index],count,n,lookup)
		else:
			if lookup[index*100+(k-(cur_sum+arr[index]))]==1:
				count[0] += 1
			
		if lookup.get((index+1)*100+(k-cur_sum))==None:
			lookup[(index+1)*100+(k-cur_sum)]=makeSumUtility(arr,index+1,k,cur_sum,count,n,lookup)
		else:
			if lookup[(index+1)*100+(k-cur_sum)]==1:
				count[0] += 1
	else:	
		if lookup.get((index+1)*100+(k-cur_sum))==None:
			lookup[(index+1)*100+(k-cur_sum)]=makeSumUtility(arr,index+1,k,cur_sum,count,n,lookup)
		else:
			if lookup[(index+1)*100+(k-cur_sum)]==1:
				count[0] += 1
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
