from unittest import TestCase
from yourtest import shell_sort


class ShellSort(TestCase):
    def test_shell_sort(self):
        data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        answer = self.sort(data)
        self.assertEqual(answer, shell_sort(data))

        data = [2050, 0, -1, 20, 100, 99, 23, 20, -10, 3, 8, 7, 20.5, 3.5, -100]
        answer = self.sort(data)
        self.assertEqual(answer, shell_sort(data))

        data = [1, 2, 3, 4, 5, 6]
        answer = self.sort(data)
        self.assertEqual(answer, shell_sort(data))

        data = [6, 5, 4, 3, 2, 1]
        answer = self.sort(data)
        self.assertEqual(answer, shell_sort(data))

        data = [10, 100, 100, 20, 30, 17, 0.5, 30, 10, -50, 100]
        answer = self.sort(data)
        self.assertEqual(answer, shell_sort(data))

        data = [10]
        answer = self.sort(data)
        self.assertEqual(answer, shell_sort(data))

        data = [20, 10]
        answer = self.sort(data)
        self.assertEqual(answer, shell_sort(data))

        data = []
        answer = self.sort(data)
        self.assertEqual(answer, shell_sort(data))

    def sort(self, data):
        new_one = data[:]
        new_one.sort()
        return new_one
