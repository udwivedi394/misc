INF = 10**10

def matrixMedian02(A):
    colL = len(A[0])
    rowL = len(A)
    median = (rowL*colL-1)/2

    ctr = 0
    pos = 0
    mini = A[0][0]
    while ctr <= median:
        mini = INF+1
        for i in range(rowL):
            rowfront = 0
            while rowfront < colL and A[i][rowfront]==INF:
                rowfront += 1

            if rowfront < colL and A[i][rowfront] < mini:
                mini = A[i][rowfront]
                pos = i*colL+rowfront
                #print "Here:",pos,mini

        ctr += 1
        row = pos/colL
        col = pos%colL
        #print "row,col:",row,col

        result = A[row][col]
        A[row][col] = INF
        #print A,pos,result
        """
        pos += 1
        row = pos/colL
        col = pos%colL
        mini = A[row][col]
        """
    #print result
    return result

def matrixMedian(A):
    colL = len(A[0])
    rowL = len(A)
    median = (rowL*colL-1)/2

    ctr = 0
    pos = 0
    mini = A[0][0]

    for i in xrange(rowL):
        A[i].append(0)

    while ctr <= median:
        mini = INF+1
        for i in xrange(rowL):
            temp_pos = A[i][-1]

            if temp_pos >= colL:
                continue

            if A[i][temp_pos] < mini:
                mini = A[i][temp_pos]
                final_row = i
                final_col = temp_pos
        
        ctr += 1

        result = A[final_row][final_col]
        A[final_row][-1] = final_col+1

    return result

A = [[1,3,5],
     [2,6,9],
     [3,6,9]]

#print matrixMedian(A)

A = [[2],[1],[4],[1],[2],[2],[5]]
#print matrixMedian(A)

A =[
  [1],
  [4],
  [3],
  [1],
  [2],
  [4],
  [4],
  [4],
  [2],
  [2],
  [1],
]
print matrixMedian(A)
