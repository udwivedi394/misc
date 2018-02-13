def multiply(A,B):
    mult = 0
    place = 0
    while B:
        if B&1:
            temp = A<<place
            mult += temp
        place += 1
        B >>= 1
    return mult

def divide(A,B):
    if A<B:
        return 0
    if A == B:
        return 1

    mult = A
    place = 0
    while B:
        if B&1:
            temp = A>>place
            mult -= temp
        place += 1
        B >>= 1
    return mult

print multiply(10,23)
print divide(23,10)
