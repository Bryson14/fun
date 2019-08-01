import sys
import os


def main(txt, pkgs):
	data = {}
	for line in reversed(list(txt)):
		line = line.split('\t')
		if line[0] in data:
			if 'BTC' in line[1]:
				data[line[0]] += float(line[3])
			elif 'Backoffice' in line[1]:
				data[line[0]] -= float(line[3])
		else:
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


