#https://www.interviewbit.com/problems/nqueens/

#1 solution
def nQueen(A):
    matrix = [['.' for i in xrange(A)] for j in xrange(A)]
    final_result = []
    nQueenUtil(matrix,0,A,final_result)
    return final_result

def nQueenUtil(matrix,col,A,final_result):
    if col >= A:
        return matrix

    for i in xrange(0,A):
        if isSafe(matrix,col,i,A):
            matrix[i][col] = 'Q'
            result = nQueenUtil(matrix,col+1,A,final_result)
            if result!=False:
                temp = []
                for stri in result:
                    temp.append(''.join(stri))
                final_result.append(temp)
            matrix[i][col] = '.'
    return False

def isSafe(matrix,col,row,A):
    #Check horizontally
    for i in xrange(A):
        if matrix[row][i] == 'Q':
            return False
    
    #Check across the diagonals

    #Check off diagonal
    offset = min(col,row)
    #print "row:",row,"col:",col,"offset:",offset,
    i,j = max(0,row-offset),max(0,col-offset)
    #print "i,j:",(i,j)
    while i < A and j < A:
        if matrix[i][j]=='Q':
            return False
        i += 1
        j += 1

    #Check principle diagonal
    offset = min(col,A-row-1)
    #print "row:",row,"col:",col,"offset:",offset,
    i,j = min(A-1,row+offset),max(0,col-offset)
    #print "i,j:",(i,j)
    while i>=0 and j<A:
        if matrix[i][j]=='Q':
            return False
        i -= 1
        j += 1
    return True

print nQueen(8)
