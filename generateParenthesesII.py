#https://www.interviewbit.com/problems/generate-all-parentheses-ii/

def generateallParenthesesII(A):
    final_arr = []
    generateallParenthesesIIUtil(A,"",0,0,0,final_arr)
    return final_arr

def generateallParenthesesIIUtil(A,stri,i,plus,minus,final_arr):
    if i>=2*A:
        final_arr.append(stri)
        return

    if plus < A:
        generateallParenthesesIIUtil(A,stri+'(',i+1,plus+1,minus,final_arr)       
    if plus > minus and minus < A:
        generateallParenthesesIIUtil(A,stri+')',i+1,plus,minus+1,final_arr)

    return

print generateallParenthesesII(3)
