"""Classify a single person."""


from numpy import *

import mlia.kNN


__author__ = 'l.jones'


def classify_person():
    """Classify a single person."""

    # Get information about person.
    percent_video = \
        float(raw_input('Percentage of time playing video games? '))
    frequent_flier_miles = \
        float(raw_input('Frequent flier miles per year? '))
    ice_cream = \
        float(raw_input('Liters of ice cream consumed per year? '))

    # Get the data
    dating_data_set, dating_labels = \
        mlia.kNN.file2matrix('../etc/datingTestSet.txt')
    normal_dating, dating_ranges, dating_minimums = \
        mlia.kNN.auto_norm(dating_data_set)

    # Classify the person.
    to_classify = array([frequent_flier_miles, percent_video, ice_cream])
    classification = \
        mlia.kNN.classify0((to_classify - dating_minimums) / dating_ranges,
                           normal_dating, dating_labels, 3)

    # Print the results
    resulting_message = ['not at all', 'in small doses', 'in large doses']
    print 'You will probably like this person: %s.' % \
          resulting_message[mlia.kNN.labels2integers([classification])[0]]


if __name__ == '__main__':
    classify_person()
