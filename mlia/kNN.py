import operator
from numpy import *

__author__ = 'l.jones'


def classify0(to_classify, training_examples, labels, k):
    """Classify to_classify using training_examples and labels."""

    # calculate differences between to_classify and each training example.
    data_set_size = training_examples.shape[0]
    differences = tile(to_classify, (data_set_size, 1)) - training_examples

    # calculate distances by squaring, summing all squared distances, and
    # taking the square root of each value.
    square_differences = differences ** 2
    square_of_distances = square_differences.sum(axis=1)
    distances = square_of_distances ** 0.5

    # calculate the indices needed to sort the distances.
    sorted_distance_indices = distances.argsort()

    # tally the votes.
    votes = {}
    for i in range(k):
        vote_i_label = labels[sorted_distance_indices[i]]
        votes[vote_i_label] = votes.get(vote_i_label, 0) + 1

    # determine the top vote getter.
    sorted_votes = sorted(votes.iteritems(), key=operator.itemgetter(1),
                          reverse=True)

    # and return its label.
    return sorted_votes[0][0]


# Utility functions.


def create_data_set():
    """Create a data set to use in testing?"""
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def file2matrix(filename):
    """Read a file into a (numpy) matrix."""

    with open(filename) as in_file:
        raw_all_lines = in_file.readlines()
        all_lines = [l.strip() for l in raw_all_lines]
        records = zeros((len(all_lines), 3))
        field_values = [l.split('\t') for l in all_lines]
        labels = [['didntLike', 'smallDoses', 'largeDoses'].index(rv[-1])
                  for rv in field_values]
        for i in range(len(field_values)):
            records[i,:] = field_values[i][:3]
        return records, labels


def auto_norm(records):
    """Normalize all fields in records to the range [0, 1]."""
    # Calculate the minimum and maximum along the zeroth dimension.
    min_values = records.min(0)
    max_values = records.max(0)

    normal_ranges = max_values - min_values
    result = zeros(shape(records))

    # Normalize the data by taking all differences from minimum, and then
    # dividing those differences by the normal_ranges.
    m = records.shape[0]
    result = records - tile(min_values, (m, 1))
    result = result / tile(normal_ranges, (m, 1))
    return result, normal_ranges, min_values


