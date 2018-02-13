def addBinaryStrings(A,B):
    ctr1 = len(A)-1
    ctr2 = len(B)-1
    
    string = ""
    carry = 0
    while ctr1 >= 0 and ctr2 >= 0:
        temp = int(A[ctr1])+int(B[ctr2])
        val = (carry+temp)%2
        carry = (carry+temp)/2
        string += str(val)
        ctr1 -= 1
        ctr2 -= 1
    while ctr1 >= 0:
        val = (carry+int(A[ctr1]))%2
        carry = (carry+int(A[ctr1]))/2
        string += str(val)
        ctr1 -= 1
    while ctr2 >= 0:
        val = (carry+int(B[ctr2]))%2
        carry = (carry+int(B[ctr2]))/2
        string += str(val)
        ctr2 -= 1
    if carry>0:
        string += str(carry)
    return string[::-1]

#print addBinaryStrings("1111010","0011")

A="1010110111001101101000"
B="1000011011000000111100110"
print addBinaryStrings(A,B)

A="0"
B="0"
print addBinaryStrings(A,B)
