import csv, json
with open('baseball_data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	info = [row for row in reader]

from pprint import pprint
pprint(info)