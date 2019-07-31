import sys
import os


class Day(object):
	def __init__(self, date, firstday=False):
		self.date = date
		self.firstday = firstday
		if date > '2019-06-01':
			self.bonus = True
		else:
			self.bonus = False
		self.pending = 0.0
		self.wallet = 0.0
		self.withdraw = 0.0
		self.funding = 0.0
		self.notes = ''

	def __str__(self):
		return self.date + "\t" + str(self.invested) + "\t" + str(self.wallet) + "\t" + str(self.pending) + "\t" + \
			str(self.withdraw) + "\t" + str(self.funding) + "\t" + self.notes


def main(txt, pkgs=0):
	last_pending = 0.0
	last_wallet = 0.0
	add_phrase = ['BTC Package bonus for Order', 'BTC Daily Dividend For Order']

	date = ''
	for line in reversed(list(txt)):
		line = line.split('\t')
		if date == line[0]:
			if




if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("ERROR\nUSAGE -- python bzreader.py TRANSACTION_FILE PKGS_FILE")
	else:
		try:
			with open(sys.argv[1]) as txt:
				print("Program starting")
				main(txt)
		except FileNotFoundError:
			print(f"File name {sys.argv[1]} not found")
			sys.exit(1)
		except IOError:
			print("something went wrong starting the program. Bye Felicia")
			sys.exit(1)

