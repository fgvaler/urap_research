import features
import parse_scores as parse

score_path = 'score_data/'
profile_path = 'profile_data/'

records = parse.parse_score_file(score_path + 'franco_scores.csv')
features = features.make_features(profile_path + 'data_analysis_random_profiles.json')

record_dict = {}
for record in records:
    record_dict[(record[0], record[1])] = [record[2], None]
for feature in features:
    if feature.id in record_dict.keys():
        record_dict[feature.id][1] = feature

id_dict = {}
for key in record_dict.keys():
    profile_id = key[0]
    if profile_id in id_dict.keys():
        id_dict[profile_id] += [record_dict[key]]
    else:
        id_dict[profile_id] = [record_dict[key]]

id_groups = [[pair for pair in group if pair[1]] for group in id_dict.values()]
data = [pair for pair in record_dict.values() if pair[1]]
    