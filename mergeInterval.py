def mergeIntervals(A,B):
	n = len(A)
	temp = [[A[i],B[i]] for i in range(n)]

	temp = sorted(temp,key=lambda item:item[0],reverse=True)
	print temp
	stack = []
	while len(temp)>1:
		top1 = temp.pop()
		top2 = temp.pop()
		
		if top2[0] < top1[1]:
			top1[1] = max(top1[1],top2[1])
			temp.append(top1)
		else:
			stack.append(top1)
			temp.append(top2)
	print stack
	print temp

A = [6,1,2,4]
B = [8,9,4,7]
A = [1,3,8]
B = [2,6,10]
mergeIntervals(A,B)
