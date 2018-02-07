def squareRoot(A):
    if A <= 1:
        return A

    start = 0
    end = A

    while start <= end:
        mid = (start+end)/2

        res = A/mid
        if res == mid:
            return mid

        if res < mid:
            end = mid-1

        if res > mid:
            start = mid+1

    return mid if mid*mid < A else mid-1

print squareRoot(226)
