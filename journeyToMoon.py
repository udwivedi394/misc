def journeyToMoon(n,astronaut):
	p = len(astronaut)
	mainset = set(astronaut[0])
	groups = [set(astronaut[0])]

	for i in range(1,p):
		pair = astronaut[i]
		val = 0 if pair[0] in mainset else -1
		if val==-1:
			val = 1 if pair[1] in mainset else -1
		if val==-1:
			groups.append(set(pair))	
	
		mainset.add(pair[0])
		mainset.add(pair[1])

		all_i = []
		for i in range(len(groups)):
			seti = groups[i]
			if pair[val] in seti:
				seti.add(pair[val^1])
				all_i.append(i)

		print all_i
	for i in range(n):
		if i not in mainset:
			mainset.add(i)
			groups.append(set([i]))
	final_arr = []
	
	sumi = 0
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
arr2 = [[0,2]]
"""
n = 10
p = 7
arr = [[0,2],[1,8],[1,4],[2,8],[2,6],[3,5],[6,9]]

print journeyToMoon(n,arr)
#print journeyToMoon(4,arr2)
