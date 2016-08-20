class Stack:
    def __init__(self, new_list = None):
        self._list = new_list if new_list else []

    def push(self, value):
        self._list.append(value)

    def pop(self):
        return self._list.pop()

    def __len__(self):
        return len(self._list)

    def peek(self):
        return self._list[-1]

    def is_empty(self):
        return len(self) <= 0

    def __repr__(self):
        return str(self._list)
