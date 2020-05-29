import parse_scores as parse
import plot

import csv
from functools import reduce
from statistics import mean

paths = ['franco_scores.csv', 'annotations_AF.csv', 'annotations_AF_new.csv', 'annotations_200+.csv', 'annotations_200+_new.csv', 'annotations.csv']
score_path = 'score_data/'

def average_score_per_exp(raw_data):
    max_exp = max([row[1] for row in raw_data])
    initial = [[] for _ in range(max_exp + 1)]

    def add_to_groups(groups, datum):
        exp = datum[1]
        score = datum[2]
        groups[exp].append(score)
        return groups

    grouped_by_exp = reduce(add_to_groups, raw_data, initial)
    averages = [mean(group) for group in grouped_by_exp]
    return averages

raw_data = [parse.parse_score_file(score_path + path) for path in paths]
averages = [average_score_per_exp(datum) for datum in raw_data]

for average in averages:
    y = average
    x = range(len(y))
    plot.scatter(x, y)
    print(average)
    print()
