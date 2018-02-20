#https://www.interviewbit.com/problems/simplify-directory-path/

def simplifyDirPath(A):
    splitVal = A.strip().split('/')
    stack = []
    for val in splitVal:
        if val == "..":
            if stack:
                stack.pop()
        elif val in (".",""):
            pass
        else:
            stack.append(val)
    return '/'+'/'.join(stack)

path = "/home/"
print simplifyDirPath(path)

path = "/a/./b/../../c/"
print simplifyDirPath(path)

path = "/../../../c/"
print simplifyDirPath(path)

path = "/home//foo/"
print simplifyDirPath(path)

path = "/"
print simplifyDirPath(path)
