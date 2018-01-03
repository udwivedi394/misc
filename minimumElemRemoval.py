#Naive Solution 
def minimumRemovals(arr, removals=0):	
	n = len(arr)

	if 2*min(arr) > max(arr):
		return removals

	minimum_removal = 457776344543

	for i in range(n):
		temp = []+arr
		temp.pop(i)
		cur_removal = minimumRemovals(temp, removals+1)
		
		minimum_removal = min(minimum_removal, cur_removal)

	return minimum_removal

#Recursive approach; Cleaner Method
def minimumRemovals02(arr):	
	n = len(arr)

	if 2*min(arr) > max(arr):
		return 0

	return min(minimumRemovals02(arr[1:])+1, minimumRemovals02(arr[:-1])+1)

#Nested solution with two loops, if we can figure out to manage min and max in constant time,
#the solution will have overall complexity of O(n^2)
def minimumRemovals03(arr):
	starting_point=0
	ending_point=0
	max_len = 0
	max_arr = None
	
	for starting_point in range(len(arr)):
		for ending_point in range(starting_point+1,len(arr)+1):
			mini = min(arr[starting_point:ending_point])
			maxi = max(arr[starting_point:ending_point])
			if 2*mini > maxi and ending_point-starting_point > max_len:
				max_arr = arr[starting_point:ending_point]
				max_len = ending_point-starting_point

	print max_arr
	return len(arr)-len(max_arr)

#Better Solution: Time Complexity: O(n^2), Constant Space
def minimumRemovals04(arr):
	maximum_length = 0
	max_start = None
	max_end = None
	for starting_point in range(len(arr)):
		min_val = arr[starting_point]
		max_val = arr[starting_point]
		for end_point in range(starting_point,len(arr)):
			min_val = min(min_val,arr[end_point])
			max_val = max(max_val,arr[end_point])
			
			#Trickiest part of solution
			#if this property is violeted then no need to pursue bigger array
			#As if the upcoming element is smallar of greater than current min or max, 
			#the condition will remain false
			if 2*min_val <= max_val:
				print "True:",arr[starting_point:end_point+1]
				break

			if 2*min_val > max_val and end_point-starting_point > maximum_length:
				maximum_length = end_point-starting_point
				max_start = starting_point
				max_end = end_point
			pass
		pass

	if max_start and max_end:
		print arr[max_start:max_end+1]
		return maximum_length
	return -1

arr1 = [4, 5, 100, 9, 10, 11, 12, 15, 200]
arr2 = [1,2,5]
print minimumRemovals(arr1)
print minimumRemovals02(arr1)
print minimumRemovals03(arr1)
print minimumRemovals04(arr1)
