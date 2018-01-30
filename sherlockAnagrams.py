import sys
from collections import *

def anagram(s1,s2):
	n = len(s1)
	if n%2 != 0:
		return -1
	alist = list(s2)
	
	alpha1 = [0]*26
	alpha2 = [0]*26
	
	offset = ord('a')
	i = 0
	while i < n:
		alpha1[ord(s1[i])-offset] += 1
		alpha2[ord(s2[i])-offset] += 1
		i += 1
	
	count = 0
	for i in xrange(26):
		temp = alpha1[i] - alpha2[i]
		count += temp
	
	if count==0:
		return True
	return False

def findAnagram(s1,s2):
	if len(s1) > len(s2):
		return 0
	i = 0
	n1 = len(s1)

	count = 0
	while i <= len(s2)-n1:
		if anagram(s1, s2[i:i+n1]):
			count += 1
		i += 1
	return count

def sherlockAndAnagrams02(s):
	n = len(s)
	i = 1
	total_count = 0
	while i < n:
		s1 = s[:i]
		remaining_string = s[i:]
		j = 0
		while j < i:
			s2 = s1[j:]
			print "s2:",s2,"RemainingString:",remaining_string
			total_count += findAnagram(s2,remaining_string)
			j += 1
		i += 1
	return total_count
    # Complete this function

def sherlockAndAnagrams02(s):
    check = defaultdict(int)
    l = len(s)
    for i in range(l):
        for j in range(i+1,l+1):
            sub = list(s[i:j])
            sub.sort()
            sub = "".join(sub)
            check[sub]+=1
    print check
    sum = 0
    for i in check:
        n = check[i]
        sum += (n*(n-1))/2
    return sum

def sherlockAndAnagrams(s):
    lookup = defaultdict(int)
    n = len(s)
    i = 0
    while i < n:
        j = i+1
	while j < n+1:
            temp = list(s[i:j])
            temp.sort()
            temp = "".join(temp)
            lookup[temp]+=1
	    j += 1
	i += 1
    totCount = 0

    for val in lookup:
        n = lookup[val]
        totCount += (n*(n-1))/2
    return totCount

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = sherlockAndAnagrams(s)
    print(result)
