#https://www.interviewbit.com/problems/different-bits-sum-pairwise/
def hammingDistance(A):
	ans = 0
	n = len(A)
	for i in range(32):
		count = 0
		for num in A:
			if num&(1<<i)!=0:
				count += 1
		ans += count*(n-count)*2
	return ans%(10**9+7)

A = [1,3,5]
print hammingDistance(A)

A = [0,2,5,7]
print hammingDistance(A)
