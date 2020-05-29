import scores_with_features
import helpers as h

data = scores_with_features.data
id_groups = scores_with_features.id_groups

def find_relevant_values(extraction_func, threshold):
    all_vals = []
    for datum in data:
        all_vals += extraction_func(datum)
    hist = h.histogram(all_vals)
    return [key for key in hist.keys() if hist[key] > threshold]

relevant_raw_skills = find_relevant_values(lambda x: x[1].raw, 80)

relevant_majors = find_relevant_values(lambda x: x[1].majors, 40)

relevant_faculties = find_relevant_values(lambda x: x[1].faculties, 40)

def features_to_list(features):
    lst = []
    pub = 1 if features.num_pubs > 0 else 0
    pat = 1 if features.num_patents > 0 else 0
    cert = features.num_certifications
    exps = features.num_experiences
    edu = features.max_edu
    t100 = 1 if features.has_top100 else 0
    elite = 1 if features.elite else 0
    lst = [pub, pat, cert, exps, edu, t100, elite]
    for skill in relevant_raw_skills:
        lst += [1 if skill in features.raw else 0]
    for major in relevant_majors:
        lst += [1 if major in features.majors else 0]
    for faculty in relevant_faculties:
        lst += [1 if faculty in features.faculties else 0]
    return lst

num_data = [[pair[0], features_to_list(pair[1])] for pair in data]
id_grouped_data = [[[pair[0], features_to_list(pair[1])] for pair in group if pair[1] != None] for group in id_groups]
varying_features = relevant_raw_skills + relevant_majors + relevant_faculties
feature_names = ['pub', 'pat', 'cert', 'exps', 'edu', 't100', 'elite'] + varying_features
num_features = len(feature_names)
possible_vals = [[0, 1], [0, 1], range(30), range(30), range(0,8), [0, 1], [0, 1]] + [[0, 1] for _ in range(len(varying_features))]
