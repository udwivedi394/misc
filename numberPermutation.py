def permuation(A,B,C):
	n = len(A)
	
	#Ist Basecase; For n=0, F(0,B,C)=0 for any B
	if n==0:
		return 0
	
	#2nd BaseCase; For B>len(C), F(n,B,C)=0 for any C
	if B > len(str(C)):
		return 0
	
	#3rd BaseCase; For B=1, all digits in A less than C
	if B==1:
		ctr = 0
		while ctr<n and A[ctr] < C:
			ctr+=1
		return ctr
	
	#4th BaseCase; For B<len(C), if 0 is not present in A, then result is n^B
	#otherwise, if 0 is present then first digit can be chosen in (n-1)ways and rest of the digits in n ways
	if B < len(str(C)):
		if A[0]!=0:
			return n**B
		return (n-1)*(n**(B-1))

	C = map(int,list(str(C)))

	ans = 0

	#In case when B==len(C)
	for i in range(B):
		j = 0
		prev_mul = 0
		
		#For ith Digit, find digits less than C[i]
		while j < n and A[j] < C[i]:
			j += 1
		
		#For first Digit, 0 is present in A 
		if i==0 and A[0]==0:
			j -= 1

		ans += j*(n**(B-i-1))
		print "i:",i,j,n,(B-i-1),ans
		
		#if ith digit is not present in A, then no number can be made further
		if C[i] not in A:
			return ans
	print ans
	return ans

A = [0,1,5]
B = 1
C = 2
permuation(A,B,C)
A = [0,1,2,5]
permuation(A,2,21)
A = [2,4,5,9]
permuation(A,4,4321)
A = [0]
print "Ans:",permuation(A,1,5)
A = [0,1,2,5]
print "Ans:",permuation(A,1,123)
A = [2,3,5,6,7,9]
print "Ans:",permuation(A,5,42950)
A = [0,1,2,3,4,5,6,7,8,9]
print "Ans:",permuation(A,5,10004)
