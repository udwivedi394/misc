def makeSum(arr,k):
	count = [0]
	n = len(arr)
	makeSumUtility(arr,0,k,0,count,n)
	return count[0]

def isSafe(arr,index,cur_sum,k,n):
	if index>=n:
		return False
	if cur_sum+arr[index] > k:
		return False
	return True

def makeSumUtility(arr,index,k,cur_sum,count,n):
	if cur_sum > k or index >= n:
		return 0
	
	if cur_sum == k:
		count[0] += 1
		return 1

	if isSafe(arr,index,cur_sum,k,n):
		makeSumUtility(arr,index,k,cur_sum+arr[index],count,n)
		makeSumUtility(arr,index+1,k,cur_sum,count,n)
	else:
		makeSumUtility(arr,index+1,k,cur_sum,count,n)
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
