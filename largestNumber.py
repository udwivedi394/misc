def largest(A):
	alpha = [str(i) for i in A]
	alpha.sort(reverse=True,cmp=lambda X,Y:cmp(X+Y,Y+X))

	sumi = 0

	#print alpha
	for i in range(len(alpha)):
		if sumi == 0:
			sumi += A[i]
			break
	"""
		XY = alpha[i]+alpha[i+1]
		YX = alpha[i+1]+alpha[i]
		
		if XY < YX:
			temp = alpha[i]
			alpha[i]=alpha[i+1]
			alpha[i+1]=temp
	print alpha

	if sumi==0:
		sumi += A[-1]
	"""
	return ''.join(alpha) if sumi else '0'

A = [ 9, 99, 999, 9999, 9998 ]
B = [12,121]
C = [0,0,0,0,0,01,0,0,0]
D = [8,89]
E = [ 412, 823, 580, 12, 220, 746, 541, 207, 603, 961, 743, 517, 747, 891, 550, 21, 991, 683, 19, 497, 584, 910, 984, 831, 335, 485, 203, 503, 448, 141, 350, 604, 380, 794, 770, 802, 747, 355, 888, 878, 219, 233, 60, 584, 648, 599, 100, 6, 423, 681, 188, 41, 413, 965, 204, 443, 896, 991, 698, 557, 813, 359, 972, 230, 497, 157, 644, 822, 16, 423 ]
print largest(A)
print largest(B)
print largest(C)
print largest(D)
print largest(E)
print "9919919849729659619108968918888788318238228138027947707477477467436986836816648644606046035995845845805575505415175034974974854484434234234141341238035935535033523323022021921207204203191881615714112100"
