import scores_with_features
import helpers as h

import statistics
import numpy as np
import matplotlib.pyplot as plt

data = scores_with_features.data


#filter options

def top100_filter(feature):
    return feature and feature.has_top100

def edu_filter(feature):
    return feature and feature.max_edu == 7

def patent_filter(feature):
    return feature and feature.num_patents > 0

def certification_filter(feature):
    return feature and feature.num_certifications > 0

def experience_filter(feature):
    return feature and feature.num_experiences > 0

def pub_filter(feature):
    return feature and feature.num_pubs > 0



def filter_by_feature(score_feature_pairs, filter):
    return [pair[0] for pair in score_feature_pairs if filter(pair[1])]

def filter_by_score(score_feature_pairs, score):
    return [pair for pair in score_feature_pairs if pair[0] == score]

def make_histogram_of_scores(data, filter):
    filtered_data = filter_by_feature(data, filter)

    print(statistics.mean(filtered_data))
    print(statistics.stdev(filtered_data))

    num_bins = 10
    plt.hist(filtered_data, num_bins, facecolor='blue', alpha=0.5)
    plt.show()

def get_top_10_skills(skills):
    skill_to_freq = {}
    for skill in skills:
        if skill in skill_to_freq.keys():
            skill_to_freq[skill] += 1
        else:
            skill_to_freq[skill] = 1
    skill_to_freq = [[key, skill_to_freq[key]] for key in skill_to_freq.keys()]
    skill_to_freq = sorted(skill_to_freq, key = lambda x: -x[1])
    return skill_to_freq[0:10]



make_histogram_of_scores(data, pub_filter)
#change filter


select_data = filter_by_score(data, 9)
#change score amount and feature attribute
industries = [datum[1].industry for datum in select_data if datum[1]]
top10 = get_top_10_skills(industries)
print()
print(top10)


select_data2 = filter_by_score(data, 1)
#change score amount and feature attribute
raw_skills = [datum[1].raw for datum in select_data2 if datum[1]]
raw_flattened = h.flatten_once(raw_skills)
top10 = get_top_10_skills(raw_flattened)
print()
print(top10)
