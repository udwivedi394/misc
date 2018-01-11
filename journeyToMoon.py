def merge_sets(groups,arr_i):
	mainreserve = set()
	while arr_i:
		i = arr_i.pop()
		temp = groups.pop(i)
		mainreserve = mainreserve.union(temp)
	groups.append(mainreserve)
	return

def journeyToMoon(n,astronaut):
	p = len(astronaut)
	mainset = set()
	groups = []

	for pair in astronaut:
		flag1 = True if pair[0] in mainset else False
		flag2 = True if pair[1] in mainset else False

		mainset.add(pair[0])
		mainset.add(pair[1])

		if flag1 and flag2:
			arr_i = []
			for i in range(len(groups)):
				seti = groups[i]
				if pair[0] in seti or pair[1] in seti:
					arr_i.append(i)
			#print "Called for:",pair
			merge_sets(groups,arr_i)

		elif flag1 or flag2:
			for i in range(len(groups)):
				if pair[0] in groups[i] or pair[1] in groups[i]:
					groups[i].add(pair[0])
					groups[i].add(pair[1])
		else:
			groups.append(set(pair))

	for i in range(n):
		if i not in mainset:
			mainset.add(i)
			groups.append(set([i]))	
	sumi = 0
	final_arr = []
	for grp in groups:
		m = len(grp)
		final_arr.append(m)
		sumi += m
	
	result = 0
	
	for i in final_arr:
		result += i*(sumi-i)

	return result/2
"""
n = 5
p = 3
arr = [[0,1],[2,3],[0,4]]
"""
arr2 = [[0,2]]
n = 10
p = 7
arr = [[0,2],[1,8],[1,4],[2,8],[2,6],[3,5],[6,9]]

#print journeyToMoon(n,arr)
print journeyToMoon(4,arr2)
