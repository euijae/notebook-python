class Queue:
    def __init__(self):
        self._list = []

    def dequeue(self):
        return self._list.pop(0)

    def enqueue(self, item):
        self._list.append(item)

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return self.__len__() == 0

    def peek(self):
        return self._list[0]

    def __str__(self):
        return 'Queue: ' + str(self._list)


q = Queue()
print(q)
q.enqueue(1)
print(q)
q.enqueue(2)
print(q)
q.enqueue(3)
print(q)
q.enqueue(4)
print(q)
q.dequeue()
print(q)
print(q.peek())
print(q.is_empty())
