import numpy as np


def matrix_add(a, b):
    l1 = [len(i) for i in a]
    l2 = [len(i) for i in b]

    if l1 != l2:
        raise ValueError('shape is different(%s != %s)' % (l1, l2))

    response = list()
    for sub1, sub2 in zip(a, b):
        response.append([i + j for i, j in zip(sub1, sub2)])
    return response


def matrix_multiply(a, b):
    na = len(a)
    ma = list(set([len(v) for v in a]))[0]
    nb = len(b)
    mb = list(set([len(v) for v in b]))[0]
    response = [[0 for j in range(mb)] for i in range(na)]
    for i in range(na):
        for j in range(mb):
            for k in range(ma):
                response[i][j] += a[i][k] * b[k][j]

    return response


def matrix_scalar_multiply(a, b):
    if not hasattr(a, '__iter__') and hasattr(b, '__iter__'):
        scalar = a
        matrix = b
    elif hasattr(a, '__iter__') and not hasattr(b, '__iter__'):
        scalar = b
        matrix = a
    else:
        raise ValueError('one argument must be a scalar type')

    for vector in matrix:
        for i in range(len(vector)):
            vector[i] *= scalar
    return matrix
