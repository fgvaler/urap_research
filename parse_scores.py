import csv
import json

def parse_score_file(path):
    f = open(path,'rt', encoding="utf8")
    data = csv.reader(f)
    data = filter(lambda row: row[3] != 0, data)
    data = [[row[0], int(row[1]), int(row[3])] for row in data]
    return data
