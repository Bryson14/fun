import sys


def bonacci_sequence(sum_length, n):
	if sum_length < 2:
		print(f"Not able to create a sequence with a sum length of {sum_length}")
		sys.exit(1)
	elif n < 0:
		print("Not able to find a negative Nth digit in Bonacci sequence.")
		sys.argv(1)
	else:
		start = ([0] * (sum_length - 1))
		start.append(1)
		for i in range(sum_length - 1, n):
			print("i: ", i)
			previous = start[i]
			print("start after adding new spot: ", start)
			start.append(previous)
			for j in range(1, n):
				print("j: ", j)
				further_back = start[i - j]
				start[i] += further_back

		print(start)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage n_bonacci_numbers.py LENGTH_OF_SUM Nth_NUMBER")
		sys.exit(1)
	else:
		bonacci_sequence(int(sys.argv[1]), int(sys.argv[2]))
