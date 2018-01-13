import time
import queensMoveinEachDirection as qy
def queensAttack(n,k,r_q,c_q,obstacles):
	moves_x = [ 0, 1, 1, 1, 0,-1,-1,-1]
	moves_y = [-1,-1, 0, 1, 1, 1, 0,-1]

	total_safe_pos = 0
	for i in range(8):
		temp_r = r_q+moves_y[i]
		temp_c = c_q+moves_x[i]
		while isSafe(n,temp_r,temp_c,obstacles):
			total_safe_pos += 1
			temp_r += moves_y[i]
			temp_c += moves_x[i]
			#print "Next_move:",(temp_r,temp_c)
			#time.sleep(0.2)
	return total_safe_pos

def isSafe(n,cur_row,cur_col,obstacles):
	if cur_row < 1 or cur_row > n or cur_col < 1 or cur_col > n:
		return False

	for i in range(len(obstacles)):
		enemy = obstacles[i]
		#print "Current Enemy",enemy,
		if enemy == [cur_row,cur_col]:
			return False
		#time.sleep(0.2)
	return True

def queensAttack02(n,k,r_q,c_q,obstacles):
       	moves_x = [ 1, 1, 0,-1,-1,-1, 0, 1]
        moves_y = [ 0, 1, 1, 1, 0,-1,-1,-1]
	total_moves = qy.maxMoves(n,r_q,c_q)
	moves_in_dir = [max(abs(total_moves[i][0]-r_q), abs(total_moves[i][1]-c_q)) for i in range(8)]

	#print total_moves
	#print moves_in_dir
	for enemy in obstacles:

			steps = obstacle_lies_in_path(total_moves[i],enemy,r_q,c_q,moves_x[i],moves_y[i])
			if steps > 0:
				#print "In, steps:",steps-1
				moves_in_dir[i] = min(moves_in_dir[i],steps-1)
				break
	#print moves_in_dir
	return sum(moves_in_dir)

def obstacle_lies_in_path(max_move,enemy,r_q,c_q,move_x,move_y):
	#print "\n",max_move,enemy,r_q,c_q,move_x,move_y
	if move_x > 0 and enemy[0] > r_q:
		if move_y > 0 and enemy[1] > c_q and abs(enemy[0]-r_q)==abs(enemy[1]-c_q):
			return min(enemy[0]-r_q, enemy[1]-c_q)
		elif move_y < 0 and enemy[1] >= max_move[1] and abs(enemy[0]-r_q)==abs(enemy[1]-c_q):
			return min(abs(enemy[0]-r_q), abs(enemy[1]-c_q))
		elif move_y == 0 and enemy[1] == c_q:
			return enemy[0]-r_q
		return -1
	if move_x < 0 and enemy[0] < r_q:
		if move_y > 0 and enemy[1] > c_q and abs(enemy[0]-r_q)==abs(enemy[1]-c_q):
			return min(abs(enemy[0]-r_q), abs(enemy[1]-c_q))
		elif move_y < 0 and enemy[1] >= max_move[1] and abs(enemy[0]-r_q)==abs(enemy[1]-c_q):
			return min(r_q-enemy[0],c_q-enemy[1])
		elif move_y == 0 and enemy[1] == c_q:
			return r_q-enemy[0]
	if move_x == 0 and enemy[0] == r_q:
		if move_y > 0 and enemy[1] >= c_q:
			return enemy[1]-c_q
		elif move_y < 0 and enemy[1] >= max_move[1]:
			return c_q-enemy[1]
	return -1
n = 5
k = 3
obstacles = [[4,2],[5,5],[2,3]]
n1 = 5
k1 = 3
obstacles1 = [[2,5],[5,1],[1,1],[2,2],[1,3]]
#print queensAttack02(n,k,5,5,obstacles1)
#print queensAttack02(n,k,4,3,obstacles)
print queensAttack02(4,0,4,4,[])
