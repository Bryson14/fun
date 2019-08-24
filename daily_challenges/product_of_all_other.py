#  Given an array of integers, return a new array such that each element at index i of the new array
#  is the product of all th numbers in the original array except the one at i
#  For example, if our input was [1, 2, 3, 4], the expected output would be [24, 12, 8, 6]

input_arr = [.23,1254,84,.0025,1548]

new_arr = []
for i in range(len(input_arr)):
	for j in range(len(input_arr)):
		if j == i:
			pass
		elif len(new_arr) <= i:
			new_arr.append(input_arr[j])
		else:
			new_arr[i] *= input_arr[j]

print(new_arr)
