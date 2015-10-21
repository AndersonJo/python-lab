from unittest import TestCase
import numpy as np
import yourtest


class MatrixTest(TestCase):
    def setUp(self):
        self.data1 = np.matrix([[1, 2, 3, 4], [0, 2, 4, 6]])
        self.data2 = np.matrix([[3, 2, 1, 0], [5, 6, 7, 8]])

        self.data3 = np.matrix([[1, 2, 3], [0, 2, 4]])
        self.data4 = np.matrix([[3, 1, 0], [6, 7, 8]])

        self.data5 = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 7, 5, 3], [0, 3, 1, 2]])

    def test_addtion(self):
        """
        Do Not use Numpy
        """
        answer1 = self.data1 + self.data2  # [[ 4  4  4  4] [ 5  8 11 14]]
        answer2 = self.data3 + self.data4  # [[ 4  3  3] [ 6  9 12]]

        my_answer1 = yourtest.matrix_add(self.data1.tolist(), self.data2.tolist())
        my_answer2 = yourtest.matrix_add(self.data3.tolist(), self.data4.tolist())
        self.assertEqual(True, (answer1 == my_answer1).all())
        self.assertEqual(True, (answer2 == my_answer2).all())

    def test_scalar_multiplication(self):
        """
        Do Not use Numpy
        """

        self.assertEqual(True, (self.data1 * 3 == yourtest.matrix_scalar_multiply(self.data1.tolist(), 3)).all())
        self.assertEqual(True, (self.data2 * -1 == yourtest.matrix_scalar_multiply(self.data2.tolist(), -1)).all())
        self.assertEqual(True, (self.data3 * 0 == yourtest.matrix_scalar_multiply(self.data3.tolist(), 0)).all())
        self.assertEqual(True, (self.data4 * 0.4 == yourtest.matrix_scalar_multiply(0.4, self.data4.tolist())).all())

    def test_multiplication(self):
        """
        Do Not use Numpy
        """

        # a * b.T  # [[10 70] [ 8 88]]
        # a.T * b  # [[ 3  2  1  0] [16 16 16 16] [29 30 31 32] [42 44 46 48]]
        # b * a.T  # [[10  8] [70 88]]
        # b.T * a  # [[ 3 16 29 42] [ 2 16 30 44] [ 1 16 31 46] [ 0 16 32 48]]
        a1 = self.data1 * self.data2.T
        a2 = self.data1.T * self.data2
        a3 = self.data2 * self.data1.T
        a4 = self.data2.T * self.data1
        self.assertEqual(True, (a1 == yourtest.matrix_multiply(self.data1.tolist(), self.data2.T.tolist())).all())
        self.assertEqual(True, (a2 == yourtest.matrix_multiply(self.data1.T.tolist(), self.data2.tolist())).all())
        self.assertEqual(True, (a3 == yourtest.matrix_multiply(self.data2.tolist(), self.data1.T.tolist())).all())
        self.assertEqual(True, (a4 == yourtest.matrix_multiply(self.data2.T.tolist(), self.data1.tolist())).all())

    def test_transpose(self):
        """
        Do Not use Numpy
        """

        # a.T   [[1 0] [2 2] [3 4] [4 6]]
        # a     [[1 2 3 4] [0 2 4 6]]

        self.assertEqual(True, (self.data1.T == yourtest.transpose(self.data1.tolist())).all())
        self.assertEqual(True, (self.data1 == yourtest.transpose(self.data1.T.tolist())).all())
        self.assertEqual(True, (self.data2.T == yourtest.transpose(self.data2.tolist())).all())
        self.assertEqual(True, (self.data2 == yourtest.transpose(self.data2.T.tolist())).all())
        self.assertEqual(True, (self.data3.T == yourtest.transpose(self.data3.tolist())).all())
        self.assertEqual(True, (self.data3 == yourtest.transpose(self.data3.T.tolist())).all())
        self.assertEqual(True, (self.data4.T == yourtest.transpose(self.data4.tolist())).all())
        self.assertEqual(True, (self.data4 == yourtest.transpose(self.data4.T.tolist())).all())

    def test_rotate(self):
        """
        Do not use Numpy
        Rotate a matrix by 90 degree
        for example
        [[1,2,3,4]
         [5,6,7,8]
         [9,8,7,6]
         [0,3,1,0]]

        the rotated one could be something like this.
        [[0,9,5,1]
         [3,8,6,2]
         [1,7,7,3]
         [0,6,8,4]]
        """

        a0 = np.rot90(self.data5, -1)
        a1 = np.rot90(self.data5, 1)
        a2 = np.rot90(self.data1, -1)
        a3 = np.rot90(self.data1, 1)
        a4 = np.rot90(self.data2, -1)
        a5 = np.rot90(self.data2, 1)
        a6 = np.rot90(self.data3, -1)
        a7 = np.rot90(self.data3, 1)
        a8 = np.rot90(self.data4, -1)
        a9 = np.rot90(self.data4, 1)

        # np.rot90(self.data5, -1)
        # [[0 9 5 1]
        #  [3 7 6 2]
        #  [1 5 7 3]
        #  [2 3 8 4]]
        #
        # np.rot90(self.data5, 1)
        # [[4 8 3 2]
        #  [3 7 5 1]
        #  [2 6 7 3]
        #  [1 5 9 0]]

        self.assertEqual(True, (a0 == yourtest.rotate(self.data5.tolist(), -1)).all())  # Counter Clockwise
        self.assertEqual(True, (a1 == yourtest.rotate(self.data5.tolist(), 1)).all())  # Clockwise
        self.assertEqual(True, (a2 == yourtest.rotate(self.data1.tolist(), -1)).all())  # Counter Clockwise
        self.assertEqual(True, (a3 == yourtest.rotate(self.data1.tolist(), 1)).all())  # Clockwise
        self.assertEqual(True, (a4 == yourtest.rotate(self.data2.tolist(), -1)).all())  # Counter Clockwise
        self.assertEqual(True, (a5 == yourtest.rotate(self.data2.tolist(), 1)).all())  # Clockwise
        self.assertEqual(True, (a6 == yourtest.rotate(self.data3.tolist(), -1)).all())  # Counter Clockwise
        self.assertEqual(True, (a7 == yourtest.rotate(self.data3.tolist(), 1)).all())  # Clockwise
        self.assertEqual(True, (a8 == yourtest.rotate(self.data4.tolist(), -1)).all())  # Counter Clockwise
        self.assertEqual(True, (a9 == yourtest.rotate(self.data4.tolist(), 1)).all())  # Clockwise
