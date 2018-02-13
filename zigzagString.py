def zigzag(A,B):
    i = 1
    m = len(A)
    string = ""
    belowstep = max(0,2*(B-1)-1)
    abovestep = 0
    while i<=B:
        j = i-1
        alternate = True
        if i==B:
            alternate = False
        while j < m:
            print (i,j),alternate,belowstep,abovestep,":",A[j]
            string += A[j]
            if alternate:
                j += belowstep+1
            else:
                j += abovestep+1
            
            if i!=1 and i!=B:
                alternate ^= True
        belowstep -= 2
        abovestep = abovestep + (1 if abovestep == 0 else 2)

        i += 1

    print string
    return string

A = "PAYPALISHIRING"
print zigzag(A,5)

A = "ABCD"
print zigzag(A,2)

print zigzag("B ",1)
