import sys
import datetime


def get_yesterday(today):
	year, month, day = today.split("-")
	yesterday = (datetime.date(int(year), int(month), int(day)) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
	return yesterday


def rolling_data(dic, day_to_check):
	yesterday = get_yesterday(day_to_check)
	if yesterday in dic:
		return yesterday
	else:
		return rolling_data(dic, yesterday)


def wallet(txt):
	data = {}
	for line in reversed(list(txt)):
		line = line.split('\t')
		if line[0] in data:  # adding to a existing day
			if 'BTC' in line[1]:
				data[line[0]] += float(line[3])
			elif 'Backoffice' in line[1]:
				data[line[0]] += float(line[3])
		elif len(data) > 0:  # starting a spot in the dictionary for a new day.
			last_transaction_day = rolling_data(data, line[0])
			amount = data[last_transaction_day] + float(line[3])
			data[line[0]] = amount

		else:  # when adding the first day in the dictionary
			data[line[0]] = float(line[3])

	for date in data:
		print(date, " : ", abs(round(data[date], 6)))


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("ERROR\nUSAGE -- python bzreader.py TRANSACTION_FILE")
	else:
		try:
			txt = ''
			with open(sys.argv[1]) as txt:
				txt = txt.readlines()
			wallet(txt)

		except FileNotFoundError:
			print(f"File name {sys.argv[1]} or {sys.argv[2]} not found")
			sys.exit(1)


