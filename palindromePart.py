#https://www.interviewbit.com/problems/palindrome-partitioning/

def palindromePartition(A):
    finalArr = []
    palindromePartitionUtil(A,"",finalArr)
    return finalArr

def palindromePartitionUtil(stri,finalArr):
    if len(stri)==0:
        return

    if stri == stri[::-1]:
        finalArr.append(stri)

    palindromePartitionUtil(stri[:1],stri[1:],finalArr)
    palindromePartitionUtil(stri[:-1],stri[-1:],finalArr)
    return

print palindromePartition("aab")
