import sys
import datetime


def main(txt, pkgs):
	data = {}
	for line in reversed(list(txt)):
		line = line.split('\t')
		if line[0] in data:  # adding to a existing day
			if 'BTC' in line[1]:
				data[line[0]] += float(line[3])
			elif 'Backoffice' in line[1]:
				data[line[0]] += float(line[3])
				print(f"backoffice {float(line[3])}")
		elif len(data) > 0:  # starting a spot in the dictionary for a new day.
			# TODO fix when in the beginning there isnt a transaction for every day
			try:
				year, month, day = line[0].split("-")
				yesterday = (datetime.date(int(year), int(month), int(day)) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
				# print(f'line[0] {line[0]}, yesterday {yesterday}')
				data[line[0]] = data[yesterday] + float(line[3])
			except KeyError:
				pass
		else:  # when adding the first day in the dictionary
			data[line[0]] = float(line[3])

	print(data)


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("ERROR\nUSAGE -- python bzreader.py TRANSACTION_FILE PKGS_FILE")
	else:
		try:
			txt = ''
			pkgs = ''
			with open(sys.argv[1]) as txt:
				txt = txt.readlines()
			with open(sys.argv[2]) as pkgs:
				pkgs = pkgs.readlines()
			main(txt, pkgs)

		except FileNotFoundError:
			print(f"File name {sys.argv[1]} or {sys.argv[2]} not found")
			sys.exit(1)


