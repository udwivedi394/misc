def palindrome(A):
    low = 0
    high = len(A)-1

    while low < high:
        if isalpha(A[low])==False:
            low += 1
            continue
        if isalpha(A[high])==False:
            high -= 1
            continue

        if A[low].lower() != A[high].lower():
            return False

        low += 1
        high -= 1
    return True

def isalpha(ch):
    if ch >= 'a' and ch <= 'z':
        return True
    if ch >= 'A' and ch <= 'Z':
        return True
    if ch >= '0' and ch <= '9':
        return True

    return False

A = "A man, a plan, a ccanal: Panama"
print palindrome(A)

A = "race a car"
print palindrome(A)

A = "Az"
print palindrome(A)

A = "1a2"
print palindrome(A)
