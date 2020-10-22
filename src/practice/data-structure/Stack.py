class Stack:
    def __init__(self):
        self._list = []

    def pop(self):
        return self._list.pop(-1)

    def push(self, item):
        self._list.append(item)

    def peek(self):
        return self._list[-1]

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return 'Stack: ' + str(self._list)


s = Stack()
print(s)
s.push(1)
print(s)
s.push(2)
print(s)
s.push(3)
print(s)
print('peek:', s.peek())
print('pop:', s.pop())
