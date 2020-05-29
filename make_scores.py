import csv
import json

import score_calc as score
import helpers as h

def load_ids(n):
    ids = {}
    indices = {}
    file1 = open('profile_data/data_analysis_random_profiles.json')
    for i in range(n):
        line = file1.readline()
        person = json.loads(line)
        unique_id = person['user_id']
        ids[i + 1] = unique_id
        indices[unique_id] = i + 1
    return ids, indices

def convert_row(r, ids):
    r = [x for x in r if x != '']
    r = [int(x) for x in r]
    if len(r) >= 3:
        return [ids[r[0]], r[1], r[2], r[3:]]
    else:
        return []

def records_from_row(row):
    user_id = row[0]
    high = row[1]
    low = row[2]
    exp_scores = row[3]
    records = []
    for i in range(len(exp_scores)):
        exp_scores_curr = exp_scores[:i + 1]
        rolling_score = score.total_score(high, low, exp_scores_curr)
        record = [user_id, i, rolling_score]
        records += [record]
    return records

ids, indices = load_ids(1000)
f = open('score_data/manual_scores.csv','rt', encoding='utf-8')
data = csv.reader(f)
data = [convert_row(row, ids) for row in data]
data = [x for x in data if x]
data = [records_from_row(row) for row in data]
data = h.flatten_once(data)
data_padded = [[ID, exp, '', score] for ID, exp, score in data]
h.write_rows_to_csv(data_padded, 'score_data/franco_scores.csv')
