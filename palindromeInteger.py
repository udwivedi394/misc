def palindorme(A):
	print A,
	temp = list(str(A))
	i,j = 0,len(temp)-1

	while i<j:
		if temp[i]!=temp[j]:
			return False
		i += 1
		j -= 1
	return True

print palindorme(123)
print palindorme(121)
print palindorme(12121)
print palindorme(1)
print palindorme(0)
