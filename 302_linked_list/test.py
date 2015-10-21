from unittest import TestCase
from node import Node
import yourtest


class LinkedListTest(TestCase):
    def setUp(self):
        self.data1 = self._create_node([10, 5, 5, 3, 16, -1, 7, 3, -1, -1, -17])
        self.data2 = self._create_node(['a', 'b', 'c', 'd', 'e'])

    def test_remove_duplicate(self):
        a1 = [10, 5, 3, 16, -1, 7, -17]
        self.assertEqual(a1, yourtest.delete_duplicate(self.data1).to_list())

    def test_remove_middle_node(self):
        """
        Delete c node without creating any new node.
        Input : a > b > c > d > e
        Result: a > b > d > e
        """
        c_node = self.data2.next.next
        yourtest.delete_middle_node(c_node)
        self.assertEqual(['a', 'b', 'd', 'e'], self.data2.to_list())

    def test_addition(self):
        """
        There are two linked lists which represent reversed numbers.
        The 1's digit is at the head of the list.
        For example 513 can be represented as 3 > 1 > 5.

        3 > 1 > 5  +  5 > 9 > 2
        = 8 > 0 > 8
        """
        a = self._create_node([3, 1, 5])
        b = self._create_node([5, 9, 2])
        self.assertEqual([8, 0, 8], yourtest.add(a, b).to_list())

    def _create_node(self, data):
        start_node = Node(data[0])
        n = start_node
        for v in data[1:]:
            n.next = Node(v)
            n = n.next
        return start_node
