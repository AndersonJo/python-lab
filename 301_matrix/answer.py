def matrix_add(m1, m2):
    r = []
    for i in range(len(m1)):
        n = []
        for j in range(len(m1[i])):
            n.append(m1[i][j] + m2[i][j])
        r.append(n)
    return r


def matrix_multiply(m1, m2):
    r = []
    for i in range(len(m1)):
        r.append([0 for l in range(len(m1))])
        for j in range(len(m1)):
            for k in range(len(m1[j])):
                r[i][j] += m1[i][k] * m2[k][j]
    return r


def matrix_scalar_multiply(m1, m2):
    if hasattr(m1, '__iter__') and not hasattr(m2, '__iter__'):
        matrix = m1
        scalar = m2
    else:
        matrix = m2
        scalar = m1

    r = []
    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[i])):
            r[i].append(matrix[i][j] * scalar)
    return r


def transpose(matrix):
    return [arr for arr in zip(*matrix)]


def rotate(matrix, direction=-1):
    if direction == -1:
        return zip(*matrix[::-1])
    return zip(*matrix)[::-1]
