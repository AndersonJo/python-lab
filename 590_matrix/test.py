from unittest import TestCase
import numpy as np
from yourtest import matrix_add, matrix_multiply, matrix_scalar_multiply


class MatrixTest(TestCase):
    def setUp(self):
        self.data1 = [[1, 2, 3, 4], [0, 2, 4, 6]]
        self.data2 = [[3, 2, 1, 0], [5, 6, 7, 8]]

        self.data3 = [[1, 2, 3], [0, 2, 4]]
        self.data4 = [[3, 1, 0], [6, 7, 8]]

    def test_addtion(self):
        a = np.matrix(self.data1)
        b = np.matrix(self.data2)
        c = np.matrix(self.data3)
        d = np.matrix(self.data4)
        answer1 = a + b
        answer2 = c + d

        my_answer1 = matrix_add(self.data1, self.data2)
        my_answer2 = matrix_add(self.data3, self.data4)
        self.assertEqual(True, (answer1 == my_answer1).all())
        self.assertEqual(True, (answer2 == my_answer2).all())

    def test_scalar_multiplication(self):
        a = np.matrix(self.data1)
        b = np.matrix(self.data2)
        c = np.matrix(self.data3)
        d = np.matrix(self.data4)

        self.assertEqual(True, (a * 3 == matrix_scalar_multiply(self.data1, 3)).all())
        self.assertEqual(True, (b * -1 == matrix_scalar_multiply(self.data2, -1)).all())
        self.assertEqual(True, (c * 0 == matrix_scalar_multiply(self.data3, 0)).all())
        self.assertEqual(True, (d * 0.4 == matrix_scalar_multiply(0.4, self.data4)).all())

    def test_multiplication(self):
        a = np.matrix(self.data1)
        b = np.matrix(self.data2)
        c = np.matrix(self.data3)
        d = np.matrix(self.data4)

        self.assertEqual(True, (a * b.T == matrix_multiply(a.tolist(), b.T.tolist())).all())
        self.assertEqual(True, (a.T * b == matrix_multiply(a.T.tolist(), b.tolist())).all())
        self.assertEqual(True, (b * a.T == matrix_multiply(b.tolist(), a.T.tolist())).all())
        self.assertEqual(True, (b.T * a == matrix_multiply(b.T.tolist(), a.tolist())).all())
