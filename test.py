#!user/bin/env python

"""
This file is a script to clean player names in my csv file. 
At first, they were listed as such:
Quincy Acy\acyqu01

I'd like them to just be listed as
"Quicy Acy"
"""

import csv

file_out = "2016_17_nba_player_data.csv"

files_in = ["nba_2016_17_player_advanced.csv", "nba_2016_17_player_per_36.csv"]

fieldnames = []
for filename in files_in:
	with open(filename, "r") as f_in:
		reader = csv.reader(f_in)
		headers = next(reader)
		for i in headers:
			if i not in fieldnames:
				fieldnames.append(i)

fieldnames = [i for i in fieldnames if i !=""]

with open(file_out, "w") as f_out:
	writer = csv.DictWriter(f_out, fieldnames=fieldnames, extrasaction="ignore")
	writer.writeheader()
	for filename in files_in:
		with open(filename, "r") as f_in:
			reader = csv.DictReader(f_in)
			for line in reader:
				writer.writerow(line)

print fieldnames