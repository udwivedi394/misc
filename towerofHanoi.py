from collections import defaultdict

if __name__=="__main__":
	N = int(raw_input().strip())
	a = map(int,raw_input().strip().split(' '))
	
	rods = defaultdict(list)
	for i in range(1,N+1):
		rods[a[i-1]].append(i)
	
