#https://www.interviewbit.com/problems/sorted-permutation-rank-with-repeats/
from collections import defaultdict


def sortedPermutationRepeats(A):
    strlookup = sorted(list(A))
    vlookup = defaultdict(int)
    
    for i in strlookup:
        vlookup[i] += 1

    i = 0
    n = len(A)
    while i < n:
        if 
    return

sortedPermutationRepeats("aaabbcdeef")
