def fullCountSort(elements):
	n = len(elements)
	mainset = set()
	lookup = {}
	for i in range(n):
		pair = elements[i]

		if pair[0] in mainset:
			lookup[pair[0]].append(i)
		else:
			lookup[pair[0]] = [i]
		mainset.add(pair[0])
	
	#print mainset
	#print lookup

	for x in range(min(mainset),max(mainset)+1):
		if x in mainset:
			inner_array = lookup[x]
			for i in inner_array:
				if i <= n/2:
					print "-",
				else:
					print elements[i][1],
	return

if __name__ == "__main__":
	n = int(raw_input().strip())
	elements = []
	for a0 in xrange(n):
		x,s = raw_input().strip().split(' ')
		x,s = [int(x),str(s)]
		elements.append([x,s])
	#print elements
	fullCountSort(elements)

