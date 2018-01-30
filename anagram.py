import sys

def anagram(s):
	n = len(s)
	if n%2 != 0:
		return -1
	s1 = s[:n/2]
	s2 = s[n/2:]
	alist = list(s2)
	
	alpha1 = [0]*26
	alpha2 = [0]*26
	
	offset = ord('a')
	i = 0
	while i < (n/2):
		alpha1[ord(s1[i])-offset] += 1
		alpha2[ord(s2[i])-offset] += 1
		i += 1
	
	count = 0
	for i in xrange(26):
		temp = alpha1[i] - alpha2[i]
		if temp > 0:
			count += temp
	return count

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagram(s)
    print(result)
