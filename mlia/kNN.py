import operator

from numpy import *


def create_data_set():
    """Create a data set to illustrate kNN algorithm.

    The data set has two components: the instances to be classified and the labels assigned to each item.
    """
    instances = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['a', 'a', 'b', 'b']
    return instances, labels


def classify0(to_classify, instances, labels, k):
    """Classify to_classify using k-nearest neighbors of the labeled (training) instances."""

    # Calculate the sorted distances.
    instances_count = instances.shape[0]
    differences = tile(to_classify, (instances_count, 1)) - instances
    differences_squared = differences ** 2
    sum_of_differences_squared = differences_squared.sum(axis=1)
    distances = sum_of_differences_squared ** 0.5
    sorted_distances_indices = distances.argsort()

    # Tally the "votes" for each class.
    class_count = {}
    for i in range(k):
        classification = labels[sorted_distances_indices[i]]
        class_count[classification] = class_count.get(classification, 0) + 1

    # Sort the "votes" from largest to smallest
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)

    # And return the class with the largest "votes"
    return sorted_class_count[0][0]