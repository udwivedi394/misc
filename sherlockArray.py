import sys

def solve(a):
	sum_right = sum(a)
	sum_left = 0

	for i in a:
		sum_right -= i
		if sum_left == sum_right:
			return "YES"
		sum_left += i
	return "NO"
    # Complete this function

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)

