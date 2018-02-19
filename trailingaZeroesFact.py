#https://www.interviewbit.com/problems/trailing-zeros-in-factorial/
def trailingZeroesFact(A):
    result = 0
    while A:
        result += A/5
        A /= 5
    return result

print trailingZeroesFact(20)
