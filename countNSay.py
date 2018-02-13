def nthCountNSay(A):
    i = 1
    seq = '1'
    while i<A:
        seq = countNSay(seq)
        i += 1
    return seq

def countNSay(A):
    new_str = ""
    digit,count = A[0],1
    for i in A[1:]+'a':
        if i!=digit:
            new_str += str(count)+str(digit)
            digit = i
            count = 1
        else:
            count += 1
    return new_str

A = "1"
#print countNSay(A)
print nthCountNSay(3)
