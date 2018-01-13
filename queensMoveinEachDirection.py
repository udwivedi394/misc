def maxMoves(n,r_q,c_q):
	moves_x = [ 1, 1, 0,-1,-1,-1, 0, 1]
	moves_y = [ 0, 1, 1, 1, 0,-1,-1,-1]
	
	max_moves = []
	for i in range(8):
		diff_x = diff_y = 0
		if moves_x[i] > 0:
			diff_x = abs(n-r_q)
		elif moves_x[i] < 0:
			diff_x = abs(1-r_q)

		if moves_y[i] > 0:
			diff_y = abs(n-c_q)
		elif moves_y[i] < 0:
			diff_y = abs(1-c_q)

		max_x,max_y = r_q+moves_x[i]*min(diff_x,diff_y), c_q+moves_y[i]*min(diff_x,diff_y)
		if moves_x[i]*moves_y[i] == 0:
			#print "Final:",i,(max_x,max_y),
			max_x, max_y = r_q+moves_x[i]*diff_x, c_q+moves_y[i]*diff_y
			#print (max_x,max_y)
		max_moves.append([max_x,max_y])
	return max_moves
"""
maxMoves(5,4,4)
maxMoves(5,1,1)
maxMoves(5,5,5)
maxMoves(5,5,1)
maxMoves(5,3,2)
"""
