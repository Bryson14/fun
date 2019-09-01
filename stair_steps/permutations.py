my_list = [1,2,3,4,5]

#  012345 , 012354, 012435, 012453, 012534, 012543, ...


def print_permutations(a):
	permutation_amount = 1
	for i in range(1, len(a) + 1):
		permutation_amount *= i
	print(f"Possible Permutation of this array is {permutation_amount}")


def print_arr(a):
	for i in a:
		print(i, end=" ")
	print()


def perm(a, length, n):
	if length == 1:
		print_arr(a)

	for i in range(length):
		perm(a, length - 1, n)

		if length & 1:
			a[0], a[length - 1] = a[length - 1], a[0]
		else:
			a[i], a[length - 1] = a[length - 1], a[i]


print_permutations(my_list)
length = len(my_list)
perm(my_list, length, length)
