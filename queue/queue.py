class Queue:
    def __init__(self, init=None):
        self._list = init if init else []

    def enqueue(self, value):
        self._list.append(value)

    def dequeue(self):
        return self._list.pop(-1)

    def __repr__(self):
        return '{}'.format(self._list)

if __name__ == '__main__':
    q = Queue([1, 2, 3, 4, 5])
    print q
    q.enqueue(6)
    print q
    print q.dequeue()
    print q
