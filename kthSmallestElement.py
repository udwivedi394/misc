import minHeap

#Return the kth smallest element in a row-wise and column-wise sorted 2D array
def kthSmallestElem(arr,k):
	heap = minHeap.MinHeap()
	for i in arr:
		for j in i:
			heap.insert(j)
	for z in range(k-1):
		heap.delete(0)

	return heap.delete(0)

arr =  [[10,20,30,40],
	[15,25,35,45],
	[24,29,37,48],
	[32,33,39,50]]

print kthSmallestElem(arr,5)
