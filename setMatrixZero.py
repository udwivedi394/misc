def setMatrixZero(A):
	row = set()
	col = set()

	m = len(A)
	n = len(A[0])

	for i in range(m):
		for j in range(n):
			if A[i][j]==0:
				row.add(i)
				col.add(i)
	for i in range(m):
		for j in range(n):
			if i in row or j in col:
				A[i][j]=0
	
	for i in range(m):
		print A[i]

	return A

A = [[1 for i in range(10)] for j in range(10)]

A[5][6] = 0
A[5][8] = 0
A[9][6] = 0
setMatrixZero(A)
