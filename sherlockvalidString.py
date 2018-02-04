#!/bin/python

import sys
from collections import defaultdict

def isValid02(s):
	alphaset = defaultdict(int)
	for ch in s:
		alphaset[ch] += 1

	#print "Alpha:",alphaset
	n = len(s)
	#t = n//len(alphaset) + (1 if n%len(alphaset)!=0 else 0)
	#print "n,t,s:",(n,t)
	#if abs(n - t*len(alphaset)) <= 1:
	#	return "YES"
	#if n%len(alphaset) > 1:
	#	return "NO"	
	t = n//len(alphaset)

	count = 0
	for ch in alphaset:
		if alphaset[ch]-t > 1:
			return "NO"
		if alphaset[ch]-t == 1:
			count += 1
	if count > 1:
		return "NO"
    # Complete this function
def isValid(s):
	alphaset = defaultdict(int)
	for ch in s:
		alphaset[ch] += 1
	freqset = defaultdict(int)
	
	for ch,freq in alphaset.iteritems():
		freqset[freq] += 1

	print "Freqset:",freqset
	print "alphaset:",alphaset

	if len(freqset) == 1:
		return "YES"

	if len(freqset) > 2:
		return "NO"

	ll = list(freqset)
	#if abs(ll[0]-ll[1])>1:
	#	return "NO"

	#if freqset[ll[0]] > 1 and freqset[ll[1]] > 1:
	#	return "NO"
	
	#if abs(ll[0]-ll[1])>1:
	#	return "NO"
	mini = None
	for freq,ch in freqset.iteritems():
		if freq == ch and freq == 1:
			return "YES"
		if ch == 1:
			mini = freq
	print "Mini:",mini,"Max:",max(ll),"Abs:",abs(ll[0] - ll[1])
	if abs(ll[0] - ll[1]) == 1 and max(ll) == mini:
		return "YES"
	return "NO"

s = raw_input().strip()
result = isValid(s)
print(result)
