#!/usr/bin/env python

"""
This file is a script to clean player names in my csv file. 
At first, they were listed as such:
Quincy Acy\acyqu01

I'd like them to just be listed as
"Quicy Acy"
"""

import csv

INPUT_FILE = "nba_2016_17_player_data.csv"
OUTPUT_FILE = "2016_17_nba_player_data.csv"

new_data = []

with open(INPUT_FILE, "rb") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data = {}
        for item in row:
            data[item] = row[item]
        strs = row["Player"].encode("string-escape")
        find_backslash = strs.find("\\")
        data["Player"] = strs[:find_backslash]
        new_data.append(data)

keys = new_data[0].keys()

with open(OUTPUT_FILE, "ab") as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(new_data)
