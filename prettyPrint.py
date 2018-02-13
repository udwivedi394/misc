def prettyPrint(A):
    arr = []
    for i in range(A):
        row = []
        for j in range(A):
            row.append(A-min(j,i)),
        arr.append(row)

    for i in range(A):
        for j in range(A-2,-1,-1):
            last = arr[i][j]
            arr[i].append(last)

    for i in range(A-2,-1,-1):
        new_row = []+arr[i]
        arr.append(new_row)

    for i in range(len(arr)):
        print arr[i]


prettyPrint(4)
