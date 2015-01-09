"""Tests recognizing handwritten digits."""

import os
import zipfile

from numpy import *

import mlia.kNN


__author__ = 'l.jones'


def extract_class(file_name):
    return os.path.splitext(os.path.split(file_name)[1])[0][0]


def get_content(archive, directory_name):
    return [i for i in archive.infolist()
            if ((i.filename.startswith(directory_name)) and
                (not i.filename.endswith('/')))]


def test_handwritten_digits():
    """Test recognition of handwritten digits."""

    archive = zipfile.ZipFile("../etc/digits.zip")

    about_training = get_content(archive, 'trainingDigits')
    m_training = len(about_training)
    training_instances = zeros((m_training, 1024))
    training_labels = []
    for i in range(m_training):
        training_file_name = about_training[i].filename
        training_labels.append(extract_class(training_file_name))
        with archive.open(training_file_name) as af:
            training_instances[i, :] = mlia.kNN.img2vector(af)

    about_testing = get_content(archive, 'testDigits')
    m_testing = len(about_testing)
    error_count = 0.0
    for i in range(m_testing):
        testing_file_name = about_testing[i].filename
        expected_class = extract_class(testing_file_name)
        with archive.open(testing_file_name) as af:
            to_classify = mlia.kNN.img2vector(af)
            predicted_class = mlia.kNN.classify0(to_classify, training_instances, training_labels, 3)
            print("Expected: %s == Predicted: %s: %s" % \
                  (expected_class, predicted_class, expected_class == predicted_class))
            if expected_class != predicted_class:
                error_count += 1

    print()
    print("Error count: %d" % error_count)
    print("Error rate: %f" % (error_count / m_testing))



if __name__ == '__main__':
    test_handwritten_digits()