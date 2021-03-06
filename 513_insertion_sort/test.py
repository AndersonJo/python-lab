from unittest import TestCase
from yourtest import insertion_sort

class InsertionSortTest(TestCase):
    def test_insertion_sort(self):
        data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
        answer = self.sort(data)
        self.assertEqual(answer, insertion_sort(data))

        data = [1, 2, 3, 4, 5, 6]
        answer = self.sort(data)
        self.assertEqual(answer, insertion_sort(data))

        data = [6, 5, 4, 3, 2, 1]
        answer = self.sort(data)
        self.assertEqual(answer, insertion_sort(data))

        data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
        answer = self.sort(data)
        self.assertEqual(answer, insertion_sort(data))

        data = [10]
        answer = self.sort(data)
        self.assertEqual(answer, insertion_sort(data))

        data = [20, 10]
        answer = self.sort(data)
        self.assertEqual(answer, insertion_sort(data))

        data = []
        answer = self.sort(data)
        self.assertEqual(answer, insertion_sort(data))

    def sort(self, data):
        new_one = data[:]
        new_one.sort()
        return new_one
