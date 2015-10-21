class Node:
    """
    Node for Singly Linked List
    """

    def __init__(self, initdata=0):
        self.data = initdata
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def to_list(self):
        return [n.data for n in self]

    def __iter__(self):
        n = self
        while n:
            yield n
            n = n.next

    def __str__(self):
        return str(' > '.join([str(n.data) for n in self]))
