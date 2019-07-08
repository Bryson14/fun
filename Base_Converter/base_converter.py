import sys
import math


def main(num, base):
	places = 0
	new_num = ""

	# finds the appropriate number of places holders
	while math.pow(base, places) <= num:
		places += 1

	# finds the correct value for each place holder
	for i in range(places - 1, -1, -1):
		val = 0
		while val * math.pow(base, i) <= num:
			val += 1
		num -= (val - 1) * math.pow(base, i)

		# converting to letters in larger base systems
		if val > 10:
			if val > 62:
				print("this base is too large for me...")
				sys.exit(1)
			elif val > 36:
				val += ord('A') - 11
			else:
				val += ord('a') - 11
			new_num = new_num + chr(val)
		else:
			new_num = new_num + str(val - 1)

	print(f"Your new number in base {base} is {new_num}")


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("USAGE: base_converter.py NUMBER BASE")
	else:
		print(f"Converting {sys.argv[1]} from base 10 to base {sys.argv[2]}...")
		main(int(sys.argv[1]), int(sys.argv[2]))
