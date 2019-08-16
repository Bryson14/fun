import sys


def main(n):
	prime = True
	i = 2
	while i <= n/2:
		if n % i == 0:
			prime = False
		i += 1

	if prime:
		print(f"{n} IS a prime number")
	else:
		print(f"{n} IS NOT a prime number")


if __name__ == "__main__":
	main(int(sys.argv[1]))
