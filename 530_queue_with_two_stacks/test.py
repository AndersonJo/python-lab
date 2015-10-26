from unittest import TestCase
from yourtest import Queue


class QueueUsingTwoStacksTest(TestCase):
    def test_queue_using_two_stacks(self):
        q = Queue()

        # Basic Test
        for i in xrange(10):
            q.enqueue(i)

        for i in xrange(10):
            self.assertEqual(i, q.dequeue())

        # Multiple dequeue, enqueue methods
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        q.dequeue()
        q.enqueue(40)
        q.enqueue(50)
        q.dequeue()
        q.enqueue(60)

        for v in [30, 40, 50, 60]:
            self.assertEqual(v, q.dequeue())

