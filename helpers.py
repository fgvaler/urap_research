
import csv
import math

def write_rows_to_csv(rows, name):
    f = open(name, 'w', newline='')
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
    f.close()

def histogram(data):
    hist = {}
    for datum in data:
        if datum in hist.keys():
            hist[datum] += 1
        else:
            hist[datum] = 0
    return hist

def weighted_avg(vals, weights):
    total = 0
    for i in range(len(vals)):
        total += vals[i] * weights[i]
    return total/sum(weights)

def flatten_once(lst):
    l = []
    for entry in lst:
        l += entry
    return l

def entropy(distr):
    ent = 0
    for prob in distr:
        if prob > 0:
            ent += (math.log(prob,2) * prob)
    return -ent