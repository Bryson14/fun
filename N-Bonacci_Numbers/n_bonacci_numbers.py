import sys


def bonacci_sequence_recur(sum_length, n, seq=[]):
	if len(seq) > n:
		print("sequence: ", seq)
	elif n < 0:
		print("Not able to find a negative Nth digit in Bonacci sequence.")
		sys.exit(1)
	elif sum_length < 2:
		print(f"Not able to create a sequence with a sum length of {sum_length}")
		sys.exit(1)
	else:
		pass

def bonacci_sequence_iter(sum_length, n):

	if sum_length < 2:
		print(f"Not able to create a sequence with a sum length of {sum_length}")
		sys.exit(1)

	elif n < 0:
		print("Not able to find a negative Nth digit in Bonacci sequence.")
		sys.exit(1)

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

	if len(sys.argv) < 3 or len(sys.argv) > 4:
		print("Usage n_bonacci_numbers.py [-r][-i] LENGTH_OF_SUM Nth_NUMBER"
		      "-r means recursion, -i iteration. default is iteration")
		sys.exit(1)

	elif len(sys.argv) == 3:
		bonacci_sequence_iter(int(sys.argv[1]), int(sys.argv[2]))
		sys.exit(1)
	elif sys.argv[1] == '-i':
		bonacci_sequence_iter(int(sys.argv[2]), int(sys.argv[3]))
		sys.exit(1)
	elif sys.argv[1] == '-r':
		bonacci_sequence_recur(int(sys.argv[2]), int(sys.argv[3]))
		sys.exit(1)
	else:
		print("unknown command")
		sys.exit(1)
