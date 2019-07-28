import sys
import os


def main(txt):
	for line in txt:
		print(line)


if __name__ == "__main__":
	print(len(sys.argv))
	if len(sys.argv) != 2:
		print("ERROR\nUSAGE -- python bzreader.py TEXTFILE")
	else:
		try:
			with open(sys.argv[1]) as txt:
				main(txt)
		except FileNotFoundError:
			print(f"File name {sys.argv[1]} not found")
			sys.exit(1)
		except IOError:
			print("something went wrong starting the program. Bye Felicia")
			sys.exit(1)

