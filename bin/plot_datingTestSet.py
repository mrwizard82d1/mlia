"""Plot the dating test set."""

import matplotlib
import matplotlib.pyplot
import mlia.kNN
from numpy import *


__author__ = 'l.jones'


if __name__ == '__main__':
    filename = "../etc/datingTestSet.txt"
    instances, labels = mlia.kNN.file2matrix(filename)
    discrete_labels = mlia.kNN.labels2integers(labels)

    label_color_map = {'didntLike': 'red', 'smallDoses': 'green', 'largeDoses': 'blue'}
    for i in range(3):
        for j in range(i + 1, 3):
            fig = matplotlib.pyplot.figure()
            ax = fig.add_subplot(111)
            scaled_labels = (array(discrete_labels) / 4.0) + 1.0
            colored_labels = array([label_color_map[l] for l in labels])
            ax.scatter(instances[:, i], instances[:, j], 15.0 * scaled_labels, colored_labels)
            matplotlib.pyplot.show() # blocking call