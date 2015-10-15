from bisect import bisect_left
from unittest import TestCase, main

from yourtest import binary_search


class BinarySearchTest(TestCase):
    def setUp(self):
        super(BinarySearchTest, self).setUp()
        self.odd_data = [10, 20, 29, 30, 31, 40, 50]
        self.even_data = [10, 20, 29, 30, 31, 40, 50, 60]

    def test_odd_data(self):
        self.assertEqual(0, self.get_answer(self.odd_data, 10))
        self.assertEqual(1, self.get_answer(self.odd_data, 20))
        self.assertEqual(2, self.get_answer(self.odd_data, 29))
        self.assertEqual(3, self.get_answer(self.odd_data, 30))
        self.assertEqual(4, self.get_answer(self.odd_data, 31))
        self.assertEqual(5, self.get_answer(self.odd_data, 40))
        self.assertEqual(6, self.get_answer(self.odd_data, 50))
        self.assertEqual(-1, self.get_answer(self.odd_data, 5150))
        self.assertEqual(-1, self.get_answer(self.odd_data, 0))
        self.assertEqual(-1, self.get_answer(self.odd_data, -3874))
        self.assertEqual(-1, self.get_answer(self.odd_data, 11))
        self.assertEqual(-1, self.get_answer(self.odd_data, 49))
        self.assertEqual(-1, self.get_answer(self.odd_data, 22.1))
        self.assertEqual(-1, self.get_answer(self.odd_data, 30.5))

        self.assertEqual(0, binary_search(self.odd_data, 10))
        self.assertEqual(1, binary_search(self.odd_data, 20))
        self.assertEqual(2, binary_search(self.odd_data, 29))
        self.assertEqual(3, binary_search(self.odd_data, 30))
        self.assertEqual(4, binary_search(self.odd_data, 31))
        self.assertEqual(5, binary_search(self.odd_data, 40))
        self.assertEqual(6, binary_search(self.odd_data, 50))
        self.assertEqual(-1, binary_search(self.odd_data, 5150))
        self.assertEqual(-1, binary_search(self.odd_data, 0))
        self.assertEqual(-1, binary_search(self.odd_data, -3874))
        self.assertEqual(-1, binary_search(self.odd_data, 11))
        self.assertEqual(-1, binary_search(self.odd_data, 49))
        self.assertEqual(-1, binary_search(self.odd_data, 22.1))
        self.assertEqual(-1, binary_search(self.odd_data, 30.5))

    def test_even_data(self):
        self.assertEqual(0, self.get_answer(self.even_data, 10))
        self.assertEqual(1, self.get_answer(self.even_data, 20))
        self.assertEqual(2, self.get_answer(self.even_data, 29))
        self.assertEqual(3, self.get_answer(self.even_data, 30))
        self.assertEqual(4, self.get_answer(self.even_data, 31))
        self.assertEqual(5, self.get_answer(self.even_data, 40))
        self.assertEqual(6, self.get_answer(self.even_data, 50))
        self.assertEqual(7, self.get_answer(self.even_data, 60))
        self.assertEqual(-1, self.get_answer(self.even_data, 5150))
        self.assertEqual(-1, self.get_answer(self.even_data, 0))
        self.assertEqual(-1, self.get_answer(self.even_data, -3874))
        self.assertEqual(-1, self.get_answer(self.even_data, 11))
        self.assertEqual(-1, self.get_answer(self.even_data, 49))
        self.assertEqual(-1, self.get_answer(self.even_data, 22.1))
        self.assertEqual(-1, self.get_answer(self.even_data, 30.5))

        self.assertEqual(0, binary_search(self.even_data, 10))
        self.assertEqual(1, binary_search(self.even_data, 20))
        self.assertEqual(2, binary_search(self.even_data, 29))
        self.assertEqual(3, binary_search(self.even_data, 30))
        self.assertEqual(4, binary_search(self.even_data, 31))
        self.assertEqual(5, binary_search(self.even_data, 40))
        self.assertEqual(6, binary_search(self.even_data, 50))
        self.assertEqual(7, binary_search(self.even_data, 60))
        self.assertEqual(-1, binary_search(self.even_data, 5150))
        self.assertEqual(-1, binary_search(self.even_data, 0))
        self.assertEqual(-1, binary_search(self.even_data, -3874))
        self.assertEqual(-1, binary_search(self.even_data, 11))
        self.assertEqual(-1, binary_search(self.even_data, 49))
        self.assertEqual(-1, binary_search(self.even_data, 22.1))
        self.assertEqual(-1, binary_search(self.even_data, 30.5))

    def get_answer(self, data, target):
        answer = bisect_left(data, target)
        return answer if answer < len(data) and data[answer] == target else -1


if __name__ == '__main__':
    main()
