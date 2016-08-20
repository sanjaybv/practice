from stack import Stack

query = Stack([7, 2, 5, 8, 2, 3, 1, 4])
buff = Stack()

print query

while not query.is_empty():
    print query
    print buff
    element = query.pop()
    if buff.is_empty() or element <= buff.peek():
        buff.push(element)
        continue
    else:
        while not buff.is_empty() and element > buff.peek():
            query.push(buff.pop())
        buff.push(element)

print buff
