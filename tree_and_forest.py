
import refine_features as r
import helpers as h

import copy
import random
from sklearn import tree
import graphviz
from sklearn.ensemble import RandomForestClassifier

data_copy = copy.deepcopy(r.id_grouped_data)
random.shuffle(data_copy)
half_len = len(data_copy) // 2
training_unflattened = data_copy[:half_len]
validation_unflattened = data_copy[half_len:]

non_binary_training = h.flatten_once(training_unflattened)
training = [[0 if pair[0] < 8 else 1, pair[1]] for pair in non_binary_training]
non_binary_validation = h.flatten_once(validation_unflattened)
validation = [[0 if pair[0] < 8 else 1, pair[1]] for pair in non_binary_validation]

training_features = [datum[1] for datum in training]
training_scores = [datum[0] for datum in training]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_features, training_scores)

validation_features = [datum[1] for datum in validation]
validation_scores = [datum[0] for datum in validation]

predictions = list(clf.predict(validation_features))

pairs = zip(validation_scores, predictions)

successes = [1 if int(pair[0]) == int(pair[1]) else 0 for pair in pairs]

successes = sum(successes)
                   
print(successes/len(predictions))
tree.plot_tree(clf)


dot_data = tree.export_graphviz(clf, out_file=None,
                      feature_names=r.feature_names,
                      filled=True, rounded=True)
graph = graphviz.Source(dot_data)
graph.render("graphs/iris")






clf = RandomForestClassifier(n_estimators=1000)
clf.fit(training_features, training_scores)

validation_features = [datum[1] for datum in validation]
validation_scores = [datum[0] for datum in validation]

predictions = list(clf.predict(validation_features))

pairs = zip(validation_scores, predictions)

successes = [1 if int(pair[0]) == int(pair[1]) else 0 for pair in pairs]

successes = sum(successes)

print(successes/len(predictions))




