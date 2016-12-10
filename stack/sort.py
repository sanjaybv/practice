from stack import Stack

arr = [7, 2, 5, 8, 2, 3, 1, 4]
query = Stack(arr)
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

def sort_stack(stack):
    buff = []
    while stack:
        temp = stack.pop()
        while buff and temp < buff[-1]:
            stack.append(buff.pop())
        buff.append(temp)

    while buff:
        stack.append(buff.pop())

arr = [7, 2, 5, 8, 2, 3, 1, 4]
print 
print arr
sort_stack(arr)
print arr
