"""Functions for decision trees."""

import math
import operator
import pickle

__author__ = 'l.jones'


def increment_instance_label_count(label_counts, instance):
    label = instance[-1]
    label_counts[label] = label_counts.get(label, 0) + 1
    return label_counts


def increment_label_count(label_counts, label):
    label_counts[label] = label_counts.get(label, 0) + 1
    return label_counts


def calculate_shannon_entropy(instances):
    """Calculate the Shannon entropy of instances."""

    count = len(instances)
    label_counts = {}
    reduce(increment_instance_label_count, instances, label_counts)

    result = 0.0
    for label in label_counts:
        probability = float(label_counts[label]) / count
        result -= probability * math.log(probability, 2)

    return result


def create_data_set():
    data_set = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']

    return data_set, labels


def split_data_set(instances, axis, value):
    """Split instances by removing items on axis equal to value."""

    result = []
    for instance in instances:
        if instance[axis] == value:
            reduced_instance = instance[:axis]
            reduced_instance.extend(instance[axis + 1:])
            result.append(reduced_instance)

    return result


def choose_feature_to_split(instances):
    """Select the feature on which to split instances by maximizing the information gain."""

    # initialize the search
    start_entropy = calculate_shannon_entropy(instances)
    maximum_information_gain = 0.0
    selected_feature = -1

    # loop over all the features (columns) but skip the label at the end
    split_instance_count = len(instances[0]) - 1
    for candidate_feature in range(split_instance_count):
        unique_feature_values = set([instance[candidate_feature] for instance in instances])
        split_entropy = 0.0
        # loop over all values of the candidate_feature (rows)
        for feature_value in unique_feature_values:
            split_instances = split_data_set(instances, candidate_feature, feature_value)
            probability_of_split = len(split_instances) / float(len(instances))
            split_entropy += probability_of_split * calculate_shannon_entropy(split_instances)

        information_gain = start_entropy - split_entropy
        if (information_gain > maximum_information_gain):
            maximum_information_gain = information_gain
            selected_feature = candidate_feature

    return selected_feature


def plurality_vote(labels):
    """Choose the most frequent label in labels."""

    popular_labels = {}
    reduce(increment_label_count, labels, popular_labels)

    sorted_labels = sorted(popular_labels.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sorted_labels[0][0]


def create_tree(instances, feature_headers):
    """Create a decision tree of instances with feature_labels."""

    # if all instances labels are the same, return the label
    labels = [instance[-1] for instance in instances]
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    # If I have no more features upon which to split the instances,
    # take a vote.
    if len(instances[0]) == 1:
        return plurality_vote(labels)

    # Create the root node
    split_feature = choose_feature_to_split(instances)
    split_feature_label = feature_headers[split_feature]
    del(feature_headers[split_feature])
    result = {split_feature_label:{}}

    # And recursively build trees without split_feature
    unique_feature_values = set([instance[split_feature] for instance in instances])
    for feature_value in unique_feature_values:
        sub_feature_headers = feature_headers[:]
        result[split_feature_label][feature_value] = \
            create_tree(split_data_set(instances, split_feature, feature_value), sub_feature_headers)

    # Finally, return the tree.
    return result

def classify(decision_tree, feature_labels, to_classify):
    """Classify to_classify using feature_labels of decision_tree."""

    root_feature_name = decision_tree.keys()[0]
    children = decision_tree[root_feature_name]
    feature_index = feature_labels.index(root_feature_name)

    for child in children:
        if to_classify[feature_index] == child:
            if type(children[child]).__name__ == 'dict':
                label = classify(children[child], feature_labels, to_classify)
            else:
                label = children[child]

    return label


def store_tree(decision_tree, filename):
    """Store decision_tree in the file named filename."""

    with open(filename, 'w') as out_file:
        pickle.dump(decision_tree, out_file)


def load_tree(filename):
    """Return a decision tree loaded from filename."""

    with open(filename) as in_file:
        return pickle.load(in_file)