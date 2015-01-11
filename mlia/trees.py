"""Functions for decision trees."""

import math

__author__ = 'l.jones'


def increment_label_count(label_counts, instance):
    label = instance[-1]
    label_counts[label] = label_counts.get(label, 0) + 1
    return label_counts


def calculate_shannon_entropy(instances):
    """Calculate the Shannon entropy of instances."""

    count = len(instances)
    label_counts = {}
    reduce(increment_label_count, instances, label_counts)

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

