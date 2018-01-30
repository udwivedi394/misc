import sys

def pairs02(k, arr):
	arr.sort()
	#lookup = {}	
	low = 0
	high = len(arr)-1
	
	while low < high:
		if arr[low]+arr[high] == k:
			print "Pair:",arr[low],arr[high]
			low += 1
			high -= 1
		elif arr[low]+arr[high] < k:
			low += 1
		else:
			high -= 1	
	return
	
def pairs(k, arr):
	lookup = set()
	totPair = 0
	for x in arr:
		y = k + x
		if y in lookup:
			print "Pair:",(x,y)
			totPair += 1
		
		if x-k <= 0:
			y = x - k
			if y in lookup:
				print "Pair:",(x,y)
				totPair += 1
		lookup.add(x)
	return totPair

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = pairs(k, arr)
    print result
