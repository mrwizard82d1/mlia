"""Script to classify the contact lenses needed by a patient."""


import pprint

import mlia.trees
import mlia.tree_plotter


__author__ = 'l.jones'


def classify_lenses():
    """Classify the contact lenses for a patient."""

    with open('../etc/lenses.txt') as in_file:
        lenses = [instance.strip().split('\t') for instance in in_file.readlines()]
        lenses_labels = ['age', 'prescript', 'astigmatic', 'tear_rate']
        lenses_tree = mlia.trees.create_tree(lenses, lenses_labels)

    pprint.pprint(lenses_tree)

    mlia.tree_plotter.create_plot(lenses_tree)


if __name__ == '__main__':
    classify_lenses()