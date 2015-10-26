from unittest import TestCase
from yourtest import HashTable

class HashTest(TestCase):
    def test_hash(self):
        d = HashTable()
        d[11] = 'cat'
        d[22] = 'hi'
        print d.data
        print d[22]
