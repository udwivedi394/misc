def uniquePaths(A,B):
    down = A-1
    right = B-1

    ans = fact(A+B-2,max(down,right))
    ans = ans/fact(min(down,right),0)
    return ans

def fact(x,y):
    mult = 1
    
    while x > y:
        mult *= x
        x -= 1
    return mult

print uniquePaths(3,7)
print uniquePaths(10,9)
