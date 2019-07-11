import sys


def main(arr: list):
	new_arr_1 = new_arr_2 = []
	arr.sort(reverse=True)
	sum_indicator = 0
	for i in range(arr):
		if sum(arr[i:]) > sum(arr[:i]):  # if more later on in the list than before
			sum_indicator = i
	new_arr_1 = arr[sum_indicator:]
	new_arr_2 = arr[:sum_indicator]
	# finds a rough divide to make the two lists


def rebalance(arr1: list, arr2: list):
	diff = sum(arr1) - sum(arr2)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("USAGE: python array_partitioning.py # [# # # #]")
		print("This divides the array into two list with the smallest possible difference between the sums of the lists")
