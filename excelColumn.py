def excelColumn(A):
	lookup = {chr(65+key):key+1 for key in range(26)}
	#print lookup

	numList = list(A)
	place = 0
	ans = 0
	while numList:
		val = numList.pop()
		ans += 26**place*lookup[val]
		place += 1
	return ans

print excelColumn('IA')
