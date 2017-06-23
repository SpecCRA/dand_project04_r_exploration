#!/usr/bin/env python

"""
This file is a script to clean player names in my csv file. 
At first, they were listed as such:
Quincy Acy\acyqu01

I'd like them to just be listed as
"Quicy Acy"
"""

import csv

OUTPUT_FILE = "2016_17_nba_player_data.csv"

new_data = []
keys = []

with open("nba_2016_17_player_advanced.csv", "rb") as f:
    reader = csv.DictReader(f)
    for row in reader:
    	data = {}
        for key in row:
            if key not in keys:
                #print key
                keys.append(key)
                for key in row:
                    data[key] = row[key]
                strs = row["Player"].encode("string-escape")
                find_backslash = strs.find("\\")
                data["Player"] = strs[:find_backslash]
	    with open("nba_2016_17_player_per_36.csv", "rb") as next_file:
	        reader01 = csv.DictReader(next_file)
	        for line in reader01:
	            for item in line:
	                if item not in keys:
	                    #print item
	                    keys.append(item)
	                    data[item] = line[item]
    print data
    new_data.append(data)

# print keys
print new_data

# with open(OUTPUT_FILE, "ab") as f:
#    dict_writer = csv.DictWriter(f, keys)
#    dict_writer.writeheader()
#    dict_writer.writerows(new_data)
