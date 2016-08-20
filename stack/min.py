class StackMin:
    def __init__(self):
        self._stack = []
        self._min_index_stack = []
    
    def push(self, value):
        self._stack.append(value)
        if not len(self._min_index_stack):
            self._min_index_stack.append(0)
            return
        if value < self._stack[self._min_index_stack[-1]]:
            self._min_index_stack.append(len(self._stack) - 1)
    
    def pop(self):
        if len(self._stack) == 0:
            return None
        if len(self._stack) - 1 == self._min_index_stack[-1]:
            self._min_index_stack.pop()
        return self._stack.pop()

    def min(self):
        return self._stack[self._min_index_stack[-1]]

if __name__ == '__main__':
    a = StackMin()
    a.push(4)
    print a.min()
    a.push(2)
    print a.min()
    a.push(5)
    print a.min()
    a.push(1)
    print a.min()
    print
    print a.pop()
    print a.pop()
    print a.pop()
    print a.pop()
    print a.pop()

