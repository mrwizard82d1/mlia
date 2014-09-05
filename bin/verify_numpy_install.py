from numpy import *


__author__ = 'l.jones'


def verify_numpy_install():
    rand_array = random.rand(4, 4)
    print 'rand_array=\n', rand_array
    rand_mat = mat(random.rand(4, 4))
    print '\nrand_mat=\n', rand_mat
    inv_rand_mat = rand_mat.I
    print '\ninv_rand_mat=\n', inv_rand_mat
    my_eye = rand_mat * inv_rand_mat
    print '\nmy_eye=\n', my_eye
    delta = my_eye - eye(4)
    print '\nmy_eye - eye(4) = ', delta


if __name__ == '__main__':
    verify_numpy_install()

