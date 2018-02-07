def rearrangeArray02(A):
	n = len(A)
	for i in range(n):
		while A[i]!=i:
			y = A[i]
			swap(A,i,y)
	return A

def rearrangeArray(A):
	n = len(A)

	for i in range(n):
		#Original Value can be obtained by modulo n, as second part is muliple of n
		A[i] = A[i]+(A[A[i]]%n)*n

	for i in range(n):
		#new Value can be obtained by dividing by n, as the first part will be truncated as A[i] < n and
		#second part is multiple of n
		A[i] = A[i]/n
	return A

def swap(A,x,y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp

A = [3,8,1,2,4,7,6,5,0]
print rearrangeArray(A)
A = [0]
print rearrangeArray(A)
A = [3,2,1,0]
print rearrangeArray(A)
A = [4,0,2,1,3]
print rearrangeArray(A)
