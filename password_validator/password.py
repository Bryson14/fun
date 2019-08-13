import sys


def length_req(password):
	if 5 <= len(password) <= 25:
		return True
	else:
		return False


def one_number(password):
	num = False
	for char in password:
		try:
			found = int(char)
			num = True
		except ValueError:
			pass
	return num


def one_special(password):
	specials = ['!', '@', '#', '$', '%', '^', '&', '*', '~', '-', '_', '(', ')', '?']
	special = False
	for char in password:
		if char in specials:
			special = True
	return special


def no_spaces(password):
	split = str(password).split(" ")
	if len(split) > 1:
		return False
	else:
		return True


def main(password):
	if length_req(password):
		print("Length Requirement --- Good")
	else:
		print("Length Requirement --- Failed")

	if one_number(password):
		print("Number Requirement --- Good")
	else:
		print("Number Requirement --- Failed")

	if one_special(password):
		print('Special Character Requirement --- Good')
	else:
		print('Special Character Requirement --- Failed')

	if no_spaces(password):
		print("No Spaces Requirement --- Good")
	else:
		print('No Spaces Requirement --- Failed')


if __name__ == '__main__':
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		print("USAGE: password.py PASSWORD")
		sys.exit(1)
