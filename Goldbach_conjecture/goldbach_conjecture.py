import sys


def main(values):
	for val in values:
		found = set([0])
		val = int(val)
		print(f"{val}:")
		for i in range(2,val):
			if is_prime(i) and is_prime(val-i) and i not in found and (val-i) not in found:
				found.add(i)
				found.add(val-i)
				print(f"{i} + {val-i}")


def is_prime(try_number):
	if try_number == 4:
		return False
	for i in range(2,try_number//2):
		if try_number % i == 0:
			return False
	return True


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: Enter one or more numbers to see the pair of every possible prime numbers that add up to that number")
	else:
		main(sys.argv[1:])
