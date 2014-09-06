import operator
from numpy import *

__author__ = 'l.jones'


def create_data_set():
    """Create a data set to use in testing?"""
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


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
