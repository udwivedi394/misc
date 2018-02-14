#https://www.interviewbit.com/problems/container-with-most-water/

def maxArea(A):
    low = 0
    n = len(A)

    max_area = 0
    while low<n:
        k = n-1
        while k>low:
            temp_area = 0
            if A[k] >= A[low]:
                temp_area = A[low]*(k-low)
                #print temp_area,
                max_area = max(max_area,temp_area)
                break           #This is the keyfactor, we cannot have more area beyond this point
            else:
                temp_area = A[k]*(k-low)
                #print temp_area,
                max_area = max(max_area,temp_area)
            k -= 1
        low += 1

    return max_area

A = [1,5,4,3]
print maxArea(A)    
