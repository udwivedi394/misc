#https://www.interviewbit.com/problems/sudoku/

def sudoku(A):
    slot = findEmptySlot(A)
    if slot == (-1,-1):
        return A
    for i in xrange(1,10):
        if isSafe(A,slot,str(i)):
            A[slot[0]][slot[1]] = str(i)
            result = sudoku(A)
            if result != False:
                return result
            A[slot[0]][slot[1]] = '.'
    return False

def findEmptySlot(A):
    for i in xrange(9):
        for j in xrange(9):
            if A[i][j]=='.':
                return (i,j)
    return (-1,-1)

def isSafe(A,slot,val):
    row,col = slot[0],slot[1]

    for i in xrange(9):
        #check in entire row and column if the value already exists
        if A[row][i] == val or A[i][col] == val:
            return False
   
    row1 = (row/3)*3
    col1 = (col/3)*3
    i = row1
    while i < row1+3:
        j = col1
        while j < col1+3:
            #print "(i,j):",(i,j)
            if A[i][j]==val:
                return False
            j += 1
        i += 1
    return True

A = [['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

print sudoku(A)
