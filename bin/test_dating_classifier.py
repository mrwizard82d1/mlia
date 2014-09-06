"""Prints results of testing classification of dating data set."""


import mlia.kNN


__author__ = 'l.jones'


def test_dating_classifier():
    """Prints the results of testing the classifier."""

    ho_ratio = 0.10
    dating_data_set, dating_labels = \
        mlia.kNN.file2matrix('etc/datingTestSet.txt')
    normalized_dating, dating_ranges, dating_minimums = \
        mlia.kNN.auto_norm(dating_data_set)
    m = normalized_dating.shape[0]
    test_vector_count = int(m * ho_ratio)
    error_count = 0.0
    for i in range(test_vector_count):
        classification_result = \
        mlia.kNN.classify0(normalized_dating[i,:],
                           normalized_dating[test_vector_count:m, :],
                           dating_labels[test_vector_count:m], 3)
        print 'Predicted %d, actual %d' % (classification_result,
                                           dating_labels[i])
        if classification_result != dating_labels[i]:
            error_count += 1

    print 'The error rate is %f' % (error_count / float(test_vector_count))


if __name__ == '__main__':
    test_dating_classifier()
