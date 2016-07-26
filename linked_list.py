class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
    def __repr__(self):
        if self.next:
            print self.next, '',
        return '<- {}'.format(self.value)

def make_list(values):
    
    head = None
    tail = None

    for value in values:
        curr = Node(value)
        if not head:
            head = curr
            tail = curr
        else:
            tail.next = curr
            tail = curr

    return head
