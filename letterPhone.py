#https://www.interviewbit.com/problems/letter-phone/

letter = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def letterPhone(A):
    final_arr = []
    letterPhoneUtil(A,0,"",final_arr)
    return final_arr

def letterPhoneUtil(A,i,stri,final_arr):
    if i == len(A):
        final_arr.append(stri)
        return

    for x in letter[int(A[i])]:
        letterPhoneUtil(A,i+1,stri+x,final_arr)
    return

A = "23"
#print letterPhone("01")
print letterPhone("12130")
