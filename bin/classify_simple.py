"""Classify points using the simple classifier (classify0)."""


import mlia.kNN


__author__ = 'l.jones'


if __name__ == '__main__':
    print("Classify [0, 0].")
    instances, labels = mlia.kNN.create_data_set()
    classification = mlia.kNN.classify0([0, 0], instances, labels, 3)
    print("Point [0, 0] is classified as: %s" % classification)