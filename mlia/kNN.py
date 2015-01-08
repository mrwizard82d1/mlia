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


def file2matrix(filename):
    """"Parses data contained in (a tab-delimited) filename into a set of labeled instances."""

    with open(filename) as data_file:
        instances_lines = data_file.readlines()

    # Initialize empty values to return (hard-coded for 3 features)
    feature_count = 3
    instances = zeros((len(instances_lines), feature_count))
    labels = []

    for (i, instance_line) in zip(range(len(instances_lines)), instances_lines):
        instance_line.strip()
        feature_values = instance_line.strip().split('\t')
        instances[i, :] = feature_values[:feature_count]
        labels.append(feature_values[-1])

    return instances, labels


def labels2integers(labels):
    """Convert the (datingTestSet) labels into integers."""

    label_map = {'didntLike': 0, 'smallDoses': 1, 'largeDoses': 2}
    return [label_map[l] for l in labels]