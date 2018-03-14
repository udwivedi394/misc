#https://www.interviewbit.com/problems/max-non-negative-subarray/

def maxset02(A):
    lookup = A[:]
    prev = 0

    change = True
    start = None
    end = None

    for i in xrange(len(lookup)):
        if lookup[i] >= 0:
            lookup[i] += prev
            prev = lookup[i]
            if change:
                start = i
                change = False
        else:
            prev = 0
            if change == False:
                end = i-1
                change = True

    if change == False:
        end = len(A)-1
    print lookup
    print start,end

def maxset(A):
    lookup = A[:]
    index = [0 for i in xrange(len(A))]

    prev = 0
    prev_index = 0
    max_result = -1000
    result_index = None
    for i in xrange(len(lookup)):
        if lookup[i] >= 0:
            lookup[i] += prev
            prev = lookup[i]
            index[i] += prev_index+1
            prev_index = index[i]

            if lookup[i] > max_result:
                max_result = lookup[i]
                result_index = i
            if lookup[i] == max_result and index[i] > index[result_index]:
                result_index = i
        else:
            prev = 0
            prev_index = 0

    print lookup
    print index
    print max_result, result_index, index[result_index],result_index-index[result_index]+1
    return A[result_index-index[result_index]+1:result_index+1]

A = [1, 2, 5, -7, 2, 3]
print maxset(A)
