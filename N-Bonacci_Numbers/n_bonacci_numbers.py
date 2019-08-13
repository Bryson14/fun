import sys


def bonacci_sequence(sum_length, n):

	if sum_length < 2:
		print(f"Not able to create a sequence with a sum length of {sum_length}")
		sys.exit(1)

	elif n < 0:
		print("Not able to find a negative Nth digit in Bonacci sequence.")
		sys.argv(1)

	else:
		# starts the list with correct amounts of 0's and 1 at the end
		start = ([0] * (sum_length - 1))
		start.append(1)

		for i in range(sum_length - 1, n - 1):  # adds new spot onto the list

			previous = start[i]
			start.append(previous)
			print("i :", i)

			for j in range(sum_length - 1):  # sums up the n digits behind the new spot
				further_back = start[i - j - 1]
				start[i + 1] += further_back

		print(start)

if __name__ == "__main__":

	if len(sys.argv) != 3:
		print("Usage n_bonacci_numbers.py LENGTH_OF_SUM Nth_NUMBER")
		sys.exit(1)

	else:
		bonacci_sequence(int(sys.argv[1]), int(sys.argv[2]))
