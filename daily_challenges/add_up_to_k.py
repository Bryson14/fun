#  given a list of numbers and a number k, return whether any two numbers from the list add up to k
#  For example, given [10, 15, 3, 7] and k = 17, return true since 7 + 10 = 17

arr1 = [10, 15, 3, 7]
arr2 = [15, 84, 95, 3, 6, 51, 78]
arr3 = [1, 2, 3, 4, 5, 6]


def main(arr, k):
	less_than = []
	greater_than = []
	too_big = []

	middle = k // 2

	for i in arr:
		if i >= k:
			too_big.append(i)
		elif i >= middle:
			for j in less_than:
				if j + i == k:
					return True
			greater_than.append(i)
		elif i < middle:
			for j in greater_than:
				if j + i == k:
					return True
			less_than.append(i)

	return False

print(main(arr2, 98))
