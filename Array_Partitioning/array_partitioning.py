import sys


def main(arr: list):
	new_arr_1 = new_arr_2 = []
	arr.sort(reverse=True)
	sum_indicator = 0
	for i in range(len(arr)):
		if sum(arr[i:]) > sum(arr[:i]):  # if more later on in the list than before
			sum_indicator = i + 1
	new_arr_1 = arr[sum_indicator:]
	new_arr_2 = arr[:sum_indicator]
	print(f"list 1 {new_arr_1} \nlist 2 {new_arr_2}")
	# finds a rough divide to make the two lists

	for i in range(len(arr)):
		rebalance(new_arr_1, new_arr_2)


def rebalance(arr1: list, arr2: list):
	diff = sum(arr1) - sum(arr2)
	print(f"diff : {diff}")
	correction = diff // 2
	if diff > 0:  # list 1 is bigger
		idx = find_closest(arr1, correction)
		arr2.append(arr1[idx])
		arr1.remove(arr1[idx])
	elif diff < 0:  # list2 is bigger
		idx = find_closest(arr2, correction)
		arr1.append(arr2[idx])
		arr2.remove(arr2[idx])
	else:
		pass
	print(f"list 1 final {arr1} \nlist 2 final {arr2}")


def find_closest(arr, correction):  # returns index of wanted value
	diff = max(arr)
	idx = 0
	for i in range(len(arr)):
		if abs(arr[i] - correction) < diff:
			diff = abs(arr[i] - correction)
			idx = i
	return idx

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("USAGE: python array_partitioning.py # [# # # #]")
		print("This divides the array into two list with the smallest possible difference between the sums of the lists")
	else:
		values = sys.argv[1:]
		values = [int(value) for value in values]
		main(values)
