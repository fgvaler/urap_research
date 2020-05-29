import csv
from scipy import stats, mean
import numpy as np

import make_scores
import processing

franco_dict = {}
franco_data = make_scores.data
james_dict = {}
james_data = []
anastassia_dict = {}
anastassia_data = []

def print_person_by_id(id):
    ind = make_scores.indices[id]
    print('PRINTING INDEX #' + str(ind))
    processing.print_person_new(ind)

def dict_to_list(d):
    m = max([int(key) for key in d.keys()])
    l = ['n/a' for x in range(int(m)+1)]
    for key in d.keys():
        l[int(key)] = int(d[key])
    return l

def list_overlap(a, b):
    overlap = list(range(min(len(a), len(b))))
    for i in range(len(overlap)):
        if a[i] == 'n/a' or b[i] == 'n/a':
            overlap[i] = 'n/a'
        else:
            overlap[i] = (a[i], b[i])
    return overlap

def dict_overlap(a, b):
    overlap = {}
    for key in a.keys():
        if key in b.keys():
            overlap[key] = list_overlap(dict_to_list(a[key]), dict_to_list(b[key]))
    return overlap

def overlap_data(a, b):
    d = dict_overlap(a, b)
    overlap = []
    for key in d.keys():
        score_list = d[key]
        for i in range(len(score_list)):
            if score_list[i] != 'n/a':
                overlap += [[key, i, int(score_list[i][0]), int(score_list[i][1])]]
    return overlap


for datum in franco_data:
    if datum[0] not in franco_dict.keys():
        franco_dict[datum[0]] = {}
    franco_dict[datum[0]][int(datum[1])] = datum[2]

with open('score_data/annotations_200+_new.csv','rt', encoding="utf8") as f:
    data = csv.reader(f)
    for row in data:
        if row[0] not in james_dict.keys():
            james_dict[row[0]] = {}
        if row[3] != 0:
            james_dict[row[0]][int(row[1])] = row[3]
            james_data += [[row[0], int(row[1]), int(row[3])]]

with open('score_data/annotations_AF_new.csv','rt', encoding="utf8") as f:
    data = csv.reader(f)
    for row in data:
        if row[0] not in anastassia_dict.keys():
            anastassia_dict[row[0]] = {}
        anastassia_dict[row[0]][int(row[1])] = row[3]
        anastassia_data += [[row[0], int(row[1]), int(row[3])]]

#franco
avg_score = mean([x[2] for x in franco_data])
people_data = []
for key in franco_dict.keys():
    people_data += [dict_to_list(franco_dict[key])]
avg_start = mean([x[0] for x in people_data])
avg_end = mean([x[-1] for x in people_data])
avg_diff = mean([abs(x[-1] - x[0]) for x in people_data])
print('Franco stats:')
print('\tavg_initial_score: ' + str(avg_start))
print('\tavg_final_score: ' + str(avg_end))
print('\tavg_improvement: ' + str(avg_diff))

#james
avg_score = mean([x[2] for x in james_data])
people_data = []
for key in james_dict.keys():
    people_data += [dict_to_list(james_dict[key])]
avg_start = mean([[y for y in x if y!='n/a'][0] for x in people_data])
avg_end = mean([[y for y in x if y!='n/a'][-1] for x in people_data])
avg_diff = mean([abs([y for y in x if y!='n/a'][0] - [y for y in x if y!='n/a'][-1]) for x in people_data])
print('James stats:')
print('\tavg_initial_score: ' + str(avg_start))
print('\tavg_final_score: ' + str(avg_end))
print('\tavg_improvement: ' + str(avg_diff))

#anastassia
avg_score = mean([x[2] for x in anastassia_data])
people_data = []
for key in anastassia_dict.keys():
    people_data += [dict_to_list(anastassia_dict[key])]
avg_start = mean([[y for y in x if y!='n/a'][0] for x in people_data])
avg_end = mean([[y for y in x if y!='n/a'][-1] for x in people_data])
avg_diff = mean([abs([y for y in x if y!='n/a'][0] - [y for y in x if y!='n/a'][-1]) for x in people_data])
print('Anastassia stats:')
print('\tavg_initial_score: ' + str(avg_start))
print('\tavg_final_score: ' + str(avg_end))
print('\tavg_improvement: ' + str(avg_diff))

#aj
over = overlap_data(anastassia_dict, james_dict)
diffs_sorted_aj = sorted(over, key=lambda x: -abs(int(x[2])-int(x[3])))
Xs = np.array([x[2] for x in over])
Ys = np.array([x[3] for x in over])
slope, intercept, r_value, p_value, std_err = stats.linregress(Xs,Ys)
rho, pval = stats.spearmanr(Xs, Ys)
print('AJ stats:')
print('\tslope: ' + str(slope))
print('\tintercept: ' + str(intercept))
print('\tstd_err: ' + str(std_err))
print('\tcorrelation: ' + str(r_value))
print('\tspearman: ' + str(rho))


#fa
over = overlap_data(franco_dict, anastassia_dict)
diffs_sorted_fa = sorted(over, key=lambda x: -abs(int(x[2])-int(x[3])))
Xs = np.array([x[2] for x in over])
Ys = np.array([x[3] for x in over])
slope, intercept, r_value, p_value, std_err = stats.linregress(Xs,Ys)
rho, pval = stats.spearmanr(Xs, Ys)
print('FA stats:')
print('\tslope: ' + str(slope))
print('\tintercept: ' + str(intercept))
print('\tstd_err: ' + str(std_err))
print('\tcorrelation: ' + str(r_value))
print('\tspearman: ' + str(rho))


#jf
over = overlap_data(james_dict, franco_dict)
diffs_sorted_jf = sorted(over, key=lambda x: -abs(int(x[2])-int(x[3])))
Xs = np.array([x[2] for x in over])
Ys = np.array([x[3] for x in over])
slope, intercept, r_value, p_value, std_err = stats.linregress(Xs,Ys)
rho, pval = stats.spearmanr(Xs, Ys)
print('JF stats:')
print('\tslope: ' + str(slope))
print('\tintercept: ' + str(intercept))
print('\tstd_err: ' + str(std_err))
print('\tcorrelation: ' + str(r_value))
print('\tspearman: ' + str(rho))

def jf_diff(i):
    print("James's Score: " + str(diffs_sorted_jf[i][2]))
    print("Franco's Score: " + str(diffs_sorted_jf[i][3]))
    print("Difference at exp: " + str(diffs_sorted_jf[i][1]))
    print_person_by_id(diffs_sorted_jf[i][0])

def fa_diff(i):
    print("Franco's Score: " + str(diffs_sorted_fa[i][2]))
    print("Anastassia's Score: " + str(diffs_sorted_fa[i][3]))
    print("Difference at exp: " + str(diffs_sorted_fa[i][1]))
    print_person_by_id(diffs_sorted_fa[i][0])

def aj_diff(i):
    print("Anastassia's Score: " + str(diffs_sorted_aj[i][2]))
    print("James's Score: " + str(diffs_sorted_aj[i][3]))
    print("Difference at exp: " + str(diffs_sorted_aj[i][1]))
    print_person_by_id(diffs_sorted_aj[i][0])


# print(james_data['8a64d054-6217-3a53-a036-ee693f8b6a8c']['3'])
# desired capabilities:
#     to show all the scores for a given id

#     to show a specific person's profile given their id

#     to show a specific persons score given their id and an exp number

# person -> list of scores for each exp


# for each data, calculate average score
# compare average scores
# compare 

# what kind of statements do I want to make?
# X consistently scores people lower than Y (what is average of all scores)
# X consistently scores people lower than Y at the end (what is average of final scores)
# X consistently scores people lower than Y st the start (what is average of starting scores)
# X consistently changes the scores by less than Y over time (avg difference between starting and final)

# pearson correlation (pairwise)
# best linear function that translates one data set into the other (pairwise)
# largest differences (pairwise)
# find all 3 overlap data sets and run analyses on each


# franco data -> dict of dicts | list of records ->
# ana    data -> dict of dicts | list of records ->
# james  data -> dict of dicts | list of records ->

# compile averages of scores over time
        