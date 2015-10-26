class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        for i in xrange(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        self.stack1.append(value)

    def dequeue(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
